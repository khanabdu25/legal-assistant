# legal-assistant

CHANGELOG:

NOV 8th, 2026:
- Hit my first parsing hurdle which is processing super long documents especially PDFs. Initially wanted to take pictures of pages one by one and feed it to AI to extract the text but realised that was super inefficient.
- Instead started using poppler-utils pdftotext command line tool, getting a few pages at a time.
- Learned that OCR can sometimes mess up, especially at the edges of pages or with italicized words. I am going in and fixing wrong spellings and being really explicit with the AI which is chunking the output of the pdf parse to not silently guess the fixes for errors but to instead bring it up to me.
- One PDF in particular since it is an amendment has the issue of strikethroughs which my command line tool does not catch. I have to go in and manually see what the condensed passage is with strikethroughs considered.

NOV 7th, 2026:
- Got started on initial stage of processing - preserving text verbatim, but getting it into a much more
structured format. Capturing every piece of metadata possible so the AI doesn't have to lookup context and category details every time.
- Each json has a list of sections. This makes it far easier to populate the databases for my goal of chunking which will be a later step.  

NOV 5th, 2026:
- Earlier was using the Chrome sources tab to try to get the full html, which worked out fine for simpler pages but for other ones it either didn't work or the html had massive noise with elements like navbars, ad images, footers with social media links, css etc cluttering the corpus. 
- Figured out how to get it from elements tab instead, by finding the main container div which contains the meat of the webpage, and expanded that recursively before copying (copy outer html). This turned out to be a much better and reliable approach.

NOV 4th, 2026:
- Started the project. Learned a lot about what RAG actually is, why a mix of structured and vector databases for a legal RAG-based assistant, the various "engines" needed for a project like this, what niche of law I want to focus on.
