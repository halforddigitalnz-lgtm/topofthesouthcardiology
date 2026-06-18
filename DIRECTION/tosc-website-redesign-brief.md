# Top of the South Cardiology — Website Redesign Brief

**Prepared for:** Halford Digital
**Date:** 18 June 2026
**Project:** Full redesign and rebuild on a new platform

---

## 1. The core problem

The current site (Rocketspark) holds most of the right information, but it's written and arranged for people who already understand how specialist referrals work. It also carries dated content — a "New for 2024" panel and a COVID-era telemedicine note about "the last few weeks" and "isolation rules" — which quietly erodes trust the moment a patient lands.

The redesign isn't about adding more. It's about **delivering the existing information in the clearest, lowest-friction way possible**, so that whoever lands — a referred patient, someone wondering if they need help, or a referring GP — finds their answer in one step.

---

## 2. Audiences (all three matter equally)

| Audience | What they're thinking | What they need fast |
|---|---|---|
| **The referred patient** | "I've been referred — what happens now? Do I need to do anything?" | Reassurance ("don't call us, we'll call you"), what to expect, how to prepare |
| **The self-referrer** | "Should I even be seeing a cardiologist? How does this work?" | Symptoms/reasons, how referral works, insurance vs self-funded, cost |
| **The GP / referrer** | "How do I refer a patient here? What do they need from me?" | Referral process, contact details, what info to include |

The design solves "everyone matters" not by cramming everything onto the homepage, but with a **front door that sorts people in one click**.

---

## 3. Information architecture — the "three doors" homepage

High on the homepage, three clear entry points:

1. **"I've been referred"** → what happens next, no need to phone, how to prepare for your appointment and tests.
2. **"I think I need to see a cardiologist"** → reasons to see one, how referral works, insurance vs self-funded, indicative costs.
3. **"I'm a GP / referrer"** → how to refer, what to include, direct contact.

Everything else (Out-patient Tests, Team, Angiography Suite, Useful Links, Contact) stays one click away in the main nav but does **not** compete for attention at the top. This single sorting step is the biggest "deliver info easily" lever on the whole site.

### Proposed sitemap

```
Home  (three doors + warmth + key reassurances)
├── For patients
│   ├── I've been referred — what happens next
│   ├── Do I need a cardiologist? (reasons / symptoms)
│   └── Costs, insurance & funding
├── Out-patient tests  (patient-language explainers)
│   ├── Echocardiogram
│   ├── 24h / patch ECG monitoring
│   ├── CT coronary angiography & calcium scoring
│   └── (others as relevant)
├── Angiography suite
├── Meet the team
├── For GPs / referrers  (how to refer)
├── Useful links
└── Contact  (locations, map, parking, hours)
```

---

## 4. Information-delivery principles (the heart of the brief)

These are the rules every page should follow.

- **One job per page, stated at the top.** A patient should know within two seconds whether they're in the right place.
- **Answer the unspoken question first.** Most arrive anxious. Lead with reassurance and the next action, then the detail.
- **Plain language, short sentences.** Replace process jargon ("authorisation," "affiliate provider") with what it means for the patient, with the formal term in brackets if needed.
- **Step-by-step over paragraphs.** The current "how to see a cardiologist" copy buries the key message. Turn the journey into a visible sequence: *Referral → We contact you → Your appointment → Your tests → Your results.*
- **Every test gets a four-line explainer:** what it is, does it hurt, how long it takes, how to prepare.
- **Surface the practical answers** patients actually ask the front desk: cost/funding, wait times, can I bring someone, parking, what to wear, do I stop my medications. An FAQ removes a real volume of phone calls.

---

## 5. Visual direction — "warm & human"

The goal is approachable and personal, not clinical-cold.

- **Real photography is the single biggest lever.** Faces of the team, the actual clinic and waiting room, the angiography suite. Empty image slots and stock-feeling visuals undermine trust; real people and real rooms build it.
- **Warm, calm palette** — soft, human tones rather than stark medical white. One clear accent colour used consistently.
- **Generous whitespace and a single clear type hierarchy.** The current site repeats headings and uses ALL-CAPS blocks that create visual noise — replace with calm spacing and sentence case throughout.
- **Friendly, consistent iconography** for the "reasons to see a cardiologist" and test sections instead of long text-only lists.
- **Introduce the people early.** Patients choose care they trust, and trust starts with seeing who will look after them — names, faces, a line of personality.
- **Show the place.** Photos (or a short clip) of arriving, the waiting room, the suite, so the first visit feels familiar before they walk in.

---

## 6. Accessibility (important for an older-skewing cardiology audience)

- Proper **alt text** on all images (currently empty).
- **Headings used structurally**, not decoratively — real H1/H2/H3 hierarchy for screen readers and for patients using enlarged text.
- **Strong colour contrast** and a base font size that holds up when zoomed.
- **Keyboard-navigable** menus and forms.
- Optional but on-brand: a brief **bilingual welcome / acknowledgement** (te reo) suits an NZ health context and signals openness. Low priority — include only if it feels natural, not forced.

---

## 7. Content clean-up (do this regardless of design)

- **Remove or re-label "New for 2024."** Present these as current services (CT coronary angiography & calcium scoring, patch monitoring, extended hours), not as dated news.
- **Rewrite the telemedicine section.** Drop the "last few weeks / isolation rules" framing; present video and phone consults as a standard, convenient option.
- **Consolidate the duplicated mission statement** into one well-placed line.
- **Tidy contact details** — make the right phone/email for each cardiologist unmistakable, and clarify the "please don't ring, we'll call you" message so it reassures rather than reads as a barrier.

---

## 8. "Before you arrive" — the site as the clinic's front door

A persistent, easy-to-find panel doing the emotional work before someone walks in:

- Map and **parking** guidance for each location (Lower Queen Street Health; Nelson Hospital).
- **What to bring** and what to expect on the day.
- **Who to contact** and how (with the urgent-vs-routine distinction made clear).
- Optional: patient reassurance / outcomes content (within NZ advertising rules for medical services) and links into heart-health and prevention education, positioning the practice as a community resource, not just a clinic.

---

## 9. Suggested build phases

1. **Content & structure** — finalise the three-door IA, rewrite copy in plain language, fix stale content.
2. **Design** — warm & human visual system, real photography shoot (team + clinic + suite).
3. **Build** — new platform, accessible and mobile-first.
4. **Polish** — FAQ, "before you arrive" panel, GP/referrer page, useful links.
5. **Pre-launch check** — accessibility audit, content review, mobile testing.

---

## 10. Two open decisions

- **Primary platform** for the rebuild (drives templating and CMS choices).
- **Photography** — is a shoot of the team and clinic in scope? It's the highest-impact visual investment and worth confirming early.
