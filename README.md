# legal-assistant

CHANGELOG:

NOV 5th, 2026:
- Earlier was using the Chrome sources tab to try to get the full html, which worked out fine for simpler pages but for other ones it either didn't work or the html had massive noise with elements like navbars, ad images, footers with social media links, css etc cluttering the corpus. 
- Figured out how to get it from elements tab instead, by finding the main container div which contains the meat of the webpage, and expanded that recursively before copying (copy outer html). This turned out to be a much better and reliable approach.

NOV 4th, 2026:
- Started the project. Learned a lot about what RAG actually is, why a mix of structured and vector databases for a legal RAG-based assistant, the various "engines" needed for a project like this, what niche of law I want to focus on.
