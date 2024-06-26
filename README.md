# AeroIntel: AI Chatbot Assistant for Government Policymakers

### Demo video running project
<img src="image/GifMaker_20240525233544975.gif" alt="Image" width="600"/>

**Overview:**

 AeroIntel is a cutting-edge RAG based AI assistant chatbot-GPT powered by OpenAI & Pathway created to aid government policymakers and high officials, especially from the Center of Atmospheric Sciences. This application delivers detailed insights and data on air quality, pollution control initiatives, and the health impacts of air pollution across India. AeroIntel 
 leverages advanced AI technologies to support informed decision-making and effective policy implementation to combat air pollution.

**End Users:**
  - *Government Officials*: High-ranking officials responsible for maintaining air quality standards and addressing environmental challenges. AeroIntel provides critical insights for identifying pollution hotspots, implementing policy changes, and making informed decisions.
  - *Environmental Agencies*: Departments and agencies monitoring air quality and executing pollution control measures. AeroIntel aids in tracking pollution levels, evaluating initiatives, and strategizing future actions.
  - *Corporate Sector*: CSR departments of companies funding environmental projects. AeroIntel offers valuable data to guide investments and measure impact.
  - *Environmental Consulting Firms*: Firms advising businesses on environmental regulations and carbon footprint reduction. AeroIntel provides up-to-date information and analytics to support their services.
  - *Research Institutions/Academic Researchers*: Scholars and scientists researching air quality, environmental science, and public health. AeroIntel supports research with robust data and analytical tools.
  - *Think Tanks*: Organizations dedicated to policy analysis and advocacy in the environmental sector. AeroIntel provides comprehensive data for policy recommendations and reports.
  - *Non-Governmental*: Environmental advocacy groups using AeroIntel for reliable data to raise awareness, campaign for policy changes, and monitor environmental health.
  - *Public Health Organizations*: NGOs focused on public health outcomes related to air quality. AeroIntel offers data on health impacts, aiding in the development of programs and policies to protect public health.
    
**Impacted Industry:**  
 Environment and Socio-Economic (Policy makers)

**Business Usecase:**
 AeroIntel is designed to be an invaluable tool for officials involved in environmental policy and management. By providing accurate, timely information, it supports efforts to mitigate air pollution and protect public health.Below are the top features/usecases that can be executed by the end users using aerointel.

1. **Air Quality Data:**
   - Access real-time and historical air quality data for various regions in India.
     
2. **Funding Information:**
   - Obtain details on funds allocated to each state for pollution control.
   - Track the impact of these funds on air quality improvements.

3. **Pollution Hotspots:**
   - Identify states and cities with high pollution levels.

4. **Health Impact Analysis:**
   - Explore the health impacts of air pollution on different populations.
   - Access studies and reports on pollution-related health issues.

5. **Interactive Chat Interface:**
   - Engage with the AI chatbot for quick answers to specific queries.
   - Receive detailed reports and summaries on requested topics.

**License:**
AeroIntel is released under the MIT License, promoting open collaboration and innovation.

## Pre-Requisites

1. For window users, you will need to download & install [Windows Subsystem for Linux](https://ubuntu.com/desktop/wsl) first. You can refer the [Tutorial Video](https://www.youtube.com/watch?v=eId6K8d0v6o) for more information regarding the installation.
2. **Windows Subsystem for Linux (WSL):**
WSL is a compatibility layer for running Linux binary executables natively on Windows. WSL 2, the latest version, uses a real Linux kernel and offers improved performance and full system call compatibility.

3. **Advantages of WSL:**
  - **Integration:** Allows running Linux applications and tools alongside Windows applications.
  - **Performance:** WSL 2 offers significant performance improvements over WSL 1 by using a real Linux kernel.
  - **Ease of Use:** Provides a seamless development environment for developers who work on both Windows and Linux.
    
4. For MAC/Linux/Debian users no specific requirements needed.
5. Since you are inside new Linux Environment, you might need to install many python libraries like pip,python3 etc.You will know once you run the aeroIntelRun.py file.
5. Also, we are using the OpenAI LLM model and encder model ,please be handy with the APIKey.

### Docker and WSL on Windows

1. **Docker:** Docker is a platform that enables developers to build, ship, and run applications in containers. Containers are lightweight, standalone, and executable packages that include 
               everything needed to run a piece of software, including the code, runtime, libraries, and system dependencies.

   - **Advantages of Docker:**
       - **Consistency:** Ensures that applications run the same way regardless of where they are deployed.
       - **Isolation:** Each container runs in its own isolated environment, preventing conflicts between dependencies.
       - **Portability:** Containers can run on any system that supports Docker, including different operating systems and cloud platforms.
       - **Efficiency:** Containers are more lightweight compared to virtual machines, sharing the host OS kernel and using fewer resources.

2. **Using Docker with WSL:** Combining Docker with WSL 2 provides a powerful and efficient development environment on Windows. Docker Desktop for Windows integrates with WSL 2 to provide a native-like Linux development experience.

3. **Install Docker Desktop:**
     - Download and install Docker Desktop for Windows from the Docker website.
     - During installation, enable the option to use the WSL 2-based engine.
     
4. **Integrate Docker with WSL:**
<img src="image/DropboxIntWsldemo.png" alt="Image" width="600"/>

5. **Install DropBox:**
     - Since we are using drop box as our context repository,we require drop box and the access token to call drop box api in order to download the context building materials.
     - Go to [DropBox oauth-guide](https://developers.dropbox.com/oauth-guide)  site to get your Dropbox access token
       
## Installation 

6. **Clone this repo**
     - git clone https://github.com/Alphawarrior21/AeroIntel.git
     - Navigate to home directory -> cd AeroIntel
     - Export Dropbox content to a 'local folder' inside the 'AeroIntel\Dropbox' folder. This can be done by running 'dropbox_script.py'. Remember , Windows users needs to run this step outside the
       Linux/WSL-2 environment, i.e in the windows shell As, we need a common root for Dropbox ( C:\Users\Sumit Chand\Dropbox) and our project folder, which is present inside the linux/WSL-2
       environment ( \\wsl.localhost\Ubuntu\home\Sumit\AeroIntel)
     - Update Access Token in `dropbox_script.py` generated from dropbox developer section in above step.
       ```python
       # Define your access token
       ACCESS_TOKEN = 'Dropbox access token'
     - Update your local_path where your application will access files for context building and your dropbox path where the files will be kept originally.This will be done inside 
       `dropbox_script.py`.
       ```python
       # Specify the Dropbox path and local folder path
        dropbox_path = 'C:\Users\Sumit Chand\Dropbox'
        local_path = '\\wsl.localhost\Ubuntu\home\sumit\AeroIntel\Dropbox'
      - We'll copy the dropbox content to this local Dropbox folder, inside our project folder.Run the `dropbox_script.py`
      - Modiy the .env file in the root directory of the project.
      - Replace the "OPENAI_API_TOKEN" value, place your OpenAI API key inside a quotation.Replace the dropbox address, use relative address of your dropbox.
        ```python
        OPENAI_API_TOKEN= "Your_OPENAI_API_KEY"
        HOST=0.0.0.0
        PORT=8080
        EMBEDDER_LOCATOR=text-embedding-ada-002
        EMBEDDING_DIMENSION=1536
        MODEL_LOCATOR=gpt-3.5-turbo
        MAX_TOKENS=200
        TEMPERATURE=0.0
        DROPBOX_LOCAL_FOLDER_PATH="./Dropbox"
      - All the important ministry documents will be placed in a common shared dropbox path which can act as a common repository for all the context training material fed to the encoder models to 
        generated embeddings. This could be made more robust in terms of the security but as for now in this project we see this dropbox directory as a golden source.
   
7. **Install the app dependencies**
        Install the required packages:   
           ```pip install --upgrade -r requirements.txt ```  
9. **Build up the Docker containers**    
        ```docker-compose build #one time task; will take time ( ~ 45 mins using iitk-sec(Highspeed-5GHz) )
           docker-compose up```
10. Once your container has been generated you would able to see in the docker app. You can run the app directly from there.
11. Run the Pathway API :
        ```python3 main.py```
12. Run the Ui via `ui.py`
       ```streamlit run ui.py```

### Technology stack Used ###

- LLM Models : OPENAI's gpt-3.5-turbo via [PATHWAY LIB WRAPPER](https://github.com/pathwaycom/llm-app)
- ENCODER MODEL : text-embedding-ada-002

**Streaming Pipeline:**
The incoming data from these sources is processed and after processing, the data is split into smaller chunks. This is necessary because it’s often more efficient to work with smaller pieces of text when performing NLP tasks. The changes in data are automatically synced to the pipeline enabling real-time Retrieval Augmented Generation (RAG) using llm-app .
Embedding:
These chunks are then embedded into a vector space using an OpenAI embedding model. Embedding converts text data into numerical vectors that capture the semantic meaning of the text.

**KNN Vector Indexing:**
The numerical vectors are indexed using a KNN (k-nearest neighbors) algorithm. In used to quickly retrieve the most relevant text chunks in response to a query based on vector similarity. The AURA is reactive to changes to the corpus of documents: once new snippets are provided, it reindexes them and starts to use the new knowledge to answer subsequent queries. This technique is significantly faster and more efficient than conducting individual comparisons between the query and every document.

**User Query Processing:**
When a user submits a query, a Spacy module is used to extract relevant keywords from the question. Spacy is an open-source software library for advanced NLP.
Concurrently, the user's question is also embedded using the same OpenAI embedding model to ensure that the question and the data chunks are in the same vector space.

**Integration of User Query and Knowledge Base:**
The embedded user query is then used to perform a KNN search in the vector index to find the most relevant chunks of embedded data from the processed sources.
This combination of user query embeddings and indexed data allows the system to understand and retrieve information that is contextually relevant to the user's question.

**Response Generation:**
The LLM (Large Language Model), uses the retrieved information to generate an appropriate response.
The response generation is likely informed by a prompt template, which structures how the model should incorporate the information into a coherent reply.






