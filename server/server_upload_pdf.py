import os
import time
import multiprocessing
import pdfplumber
from helper_store_vector import upload_to_faiss
import asyncio


async def main(directory):
    while True:
        files = os.listdir(directory)
        pdf_files = [f for f in files if f.endswith('.pdf')]
        
        if pdf_files:
            for pdf_file in pdf_files:
                file_path = os.path.join(directory, pdf_file)
                await upload_to_faiss(file_path)
                os.remove(file_path)
        else:
            pass
            # Get the number of CPU cores
            # num_cores = multiprocessing.cpu_count()
            # pool = multiprocessing.Pool(processes=num_cores)
            
            # for pdf_file in pdf_files:
            #     file_path = os.path.join(directory, pdf_file)
            #     pool.apply_async(read_pdf, args=(file_path,))
            
            # pool.close()
            # pool.join()

if __name__ == "__main__":
    directory = "../pdf_qa_website/media/pdf_files"
    asyncio.run(main(directory))
