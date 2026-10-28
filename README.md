# No Crown Dentistry masterclass pages

Registration page (`index.html`) and confirmation page (`thank-you.html`) for the free live masterclass
"Your Next Crown Prep Can Be an Overlay" with Dr. Rashad Riman (SurgicalMaster), Friday, November 13, 2026, 5:30 PM Pacific.

Static HTML, deployed on Vercel (clean URLs: `/`, `/list` and `/thank-you`). Built and maintained by Living Well Professionals.

- `/` takes the Kajabi **Ads** form (2149766748); `/list` (`list.html`, noindexed) is the email-list copy with the **List** form (2149766749), so each registration is tagged by source. **Edit `index.html` only, then run `python build-list.py`** and commit both.
- The Kajabi embed uses `document.write`, so it must stay an inline `<script>` in the HTML. Kajabi redirects to a Kajabi landing page that forwards to `/thank-you`.
- Meta pixel: Surgical Master's Pixel (545015012327692). PageView on every page, CompleteRegistration on `/thank-you` (Kajabi's own pixel already fires Lead on the form).
- Still placeholders: the two videos, and the masterclass date (Friday, November 13, 5:30 PM PT) until Rashad confirms.
