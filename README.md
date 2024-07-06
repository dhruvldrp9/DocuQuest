# DocuQuest

DocuQuest makes it simple to dive deep into your PDFs. Just upload your documents, and DocuQuest goes to work, pulling out key details using smart technology. It stores everything securely with Supabase, so you can find what you need fast. Whether you're looking for specific answers or exploring new ideas, DocuQuest uses advanced tools to help you uncover insights effortlessly.

DocuQuest is your partner in making document management smarter and more intuitive, putting the power of sophisticated analysis right at your fingertips.

![Project Cover](https://github.com/dhruvldrp9/DocuQuest/blob/main/pdf_qa_website/DCUeest.jpeg)

## Prerequisites

Before you begin, ensure you have the following installed or set up:

1. **Python 3**: Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Supabase Account**: You'll need a Supabase account to use the vector store feature for storing PDFs and enabling search functionality.

3. **Supabase Credentials**: Obtain your Supabase credentials (API keys or tokens) to authenticate your application with Supabase.

   - Sign up for a Supabase account at [supabase.io](https://supabase.io/).
   - Navigate to your Supabase project and find or generate the necessary API keys or tokens.

## Integration Reference

For detailed instructions on integrating with Supabase's vector store, refer to the [Supabase Documentation](https://python.langchain.com/v0.2/docs/integrations/vectorstores/supabase/).

## Usage

Provide instructions on how to use your application to interact with the Supabase vector store, such as uploading PDFs and querying documents.


## Installation

To get started with **Project Name**, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dhruvldrp9/DocuQuest.git
   cd your-repository
2. **Make and activate environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
3. **Export Supabase credential:**

   ```bash
   export supabase_url="Your_supabase_url"
   export supabase_key="Your_supabase_key"
4. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
5. **Run Server:**

   ```bash
   cd server
   python3 server_upload_pdf.py
6. **In other Terminal:**

   ```bash
   uvicorn server_qa:app --port 8001
7. **In Other Terminal:**
   ```bash
   cd pdf_qa_website
   python3 manage.py migrate
   python3 manage.py runserver
