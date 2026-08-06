"""Strip the consent-form pages from the PCI PDF and correct the running footer.

The source document is 4 pages: 1-2 are the consent form (which the clinic says is not
required), 3-4 are the patient information they want to keep. Removing the first two
pages leaves the old "3 of 4 pages / PRIVATE PCI consent form" footer behind, so it is
painted over and replaced.

The source page streams leave the graphics-state stack pushed (unbalanced `q`), so the
overlay emits matching `Q` operators first — otherwise it would inherit a stale CTM and
land in the wrong place.
"""
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject, ContentStream, DecodedStreamObject, DictionaryObject, NameObject,
)

SRC = 'consent.pdf'
OUT = '/Users/tomlekkerkerker/Sites/topofthesouthcardiology/documents/angiogram-patient-information.pdf'
TITLE = 'Patient Information for Private Cardiac Angiography and Angioplasty with Stent Placement'

reader = PdfReader(SRC)
writer = PdfWriter()
for page in reader.pages[2:]:
    writer.add_page(page)

total = len(writer.pages)

for i, page in enumerate(writer.pages, start=1):
    # Properly tokenise the stream to measure how deep the graphics stack is left.
    cs = ContentStream(page.get_contents(), writer)
    depth = 0
    for _operands, op in cs.operations:
        if op == b'q':
            depth += 1
        elif op == b'Q':
            depth = max(0, depth - 1)

    res = page[NameObject('/Resources')]
    fonts = res.get('/Font')
    if fonts is None:
        fonts = DictionaryObject()
        res[NameObject('/Font')] = fonts
    fonts = fonts.get_object()
    fonts[NameObject('/FooterHelv')] = DictionaryObject({
        NameObject('/Type'): NameObject('/Font'),
        NameObject('/Subtype'): NameObject('/Type1'),
        NameObject('/BaseFont'): NameObject('/Helvetica'),
    })

    label = f'Page {i} of {total}  -  Patient information: cardiac angiography and angioplasty'
    overlay = DecodedStreamObject()
    overlay.set_data((
        'Q\n' * depth +                # unwind whatever the page left pushed
        'q\n'
        '1 0 0 1 0 0 cm\n'             # explicit identity CTM
        '1 1 1 rg\n'
        '40 44 520 30 re f\n'          # cover the old consent-form footer band
        'BT\n'
        '/FooterHelv 9 Tf\n'
        '0.4 0.4 0.4 rg\n'
        f'70.9 58 Td\n({label}) Tj\n'
        'ET\n'
        'Q\n'
    ).encode('latin-1'))

    contents = page[NameObject('/Contents')]
    existing = contents if isinstance(contents, ArrayObject) else ArrayObject([contents])
    existing.append(writer._add_object(overlay))
    page[NameObject('/Contents')] = existing
    print(f'page {i}: unwound {depth} graphics level(s)')

writer.add_metadata({'/Title': TITLE, '/Producer': 'Top of the South Cardiology'})
with open(OUT, 'wb') as fh:
    writer.write(fh)

print('written pages:', len(PdfReader(OUT).pages))
