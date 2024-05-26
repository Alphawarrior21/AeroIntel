# AeroIntel: AI Chatbot Assistant for Government Policymakers

**Overview:**
AeroIntel is a cutting-edge RAG based AI assistant chatbot-GPT powered by OpenAI & Pathway created to aid government policymakers and high officials, especially from the Center of Atmospheric Sciences. This application delivers detailed insights and data on air quality, pollution control initiatives, and the health impacts of air pollution across India. AeroIntel leverages advanced AI technologies to support informed decision-making and effective policy implementation to combat air pollution.

**End Users:**
  - *Government Officials*: Ministers and Policy Makers: High-ranking government officials responsible for maintaining air quality standards and addressing environmental and climate challenges. AeroIntel serves as a one-stop platform for these officials, providing them with critical insights to identify pollution hotspots, implement major policy changes, and make 
                            informed decisions.
  - *Environmental Agencies*: Departments and agencies tasked with monitoring air quality, executing pollution control measures, and ensuring compliance with environmental regulations. AeroIntel aids these agencies in tracking pollution levels, evaluating the effectiveness of initiatives, and strategizing future actions.
  - *Corporate Sector*: Corporate Social Responsibility (CSR) Departments: Companies engaged in CSR initiatives aimed at funding research and projects related to environmental protection, air quality improvement, and climate change mitigation. AeroIntel provides these departments with valuable data and insights to guide their investments and measure the impact of 
                        their contributions.
  - *Environmental Consulting Firms*: Firms that offer advisory services to businesses on how to comply with environmental regulations and reduce their carbon footprint. AeroIntel equips these firms with up-to-date information and analytics to support their recommendations and enhance their service offerings.
  - *Research Institutions/Academic Researchers*: Scholars and scientists conducting research on air quality, environmental science, and public health. AeroIntel provides a robust data source and analytical tool to support their research projects, facilitate data-driven conclusions, and promote interdisciplinary studies.
  - *Think Tanks*: Organizations dedicated to policy analysis and advocacy in the environmental sector. AeroIntel helps these think tanks by providing comprehensive data and insights needed to develop policy recommendations, publish reports, and influence public opinion and policy.
  - *Non-Governmental Organizations (NGOs)/nvironmental NGOs*: Organizations focused on environmental advocacy and activism. AeroIntel aids these NGOs in their efforts to raise awareness, campaign for policy changes, and monitor environmental health by providing reliable data and actionable insights.
  - *Public Health Organizations*: NGOs dedicated to improving public health outcomes related to air quality and pollution. AeroIntel offers data on the health impacts of air pollution, helping these organizations to develop programs and advocate for policies that protect public health.

**Business Usecase:**
AeroIntel is designed to be an invaluable tool for officials involved in environmental policy and management. By providing accurate, timely information, it supports efforts to mitigate air pollution and protect public health.Below are the top features/usecases that can be executed by the end users using aerointel.

1. **Air Quality Data:**
   - Access real-time and historical air quality data for various regions in India.
   - Visualize trends and patterns through interactive charts and graphs.

2. **Funding Information:**
   - Obtain details on funds allocated to each state for pollution control.
   - Track the impact of these funds on air quality improvements.

3. **Pollution Hotspots:**
   - Identify states and cities with high pollution levels.
   - Receive alerts on critical pollution events and emerging hotspots.

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
<Image of resource>

5. **Install DropBox:**
     - Since we are using drop box as our context repository,we require drop box and the access token to call drop box api in order to download the context building materials.
     - Go to [DropBox oauth-guide](https://developers.dropbox.com/oauth-guide)  site to get your Dropbox access token
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
        ```python
        pip install --upgrade -r requirements.txt
   8. **Build up the Docker containers**
        ```python
        docker-compose build #one time task; will take time ( ~ 45 mins using iitk-sec(Highspeed-5GHz) )
        docker-compose up
    9. Once your container has been generated you would able to see in the docker app. You can run the app directly from there.
    10. Run the Pathway API :
        ```python
        python3 main.py
    12. Run the Ui via `ui.py`
        ```python
        streamlit run ui.py
