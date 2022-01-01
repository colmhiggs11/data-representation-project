<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/colmhiggs11/Machine_Learning_21_CH">
  </a>
  
<h1 align="center">Data Representation Flask App project  </h1>

  <img alt="img" src="https://miro.medium.com/max/792/1*lJ32Bl-lHWmNMUSiSq17gQ.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="img" src="https://devopedia.org/images/article/140/9072.1547744489.png" width="30%">
</p>

<p align="center">
     Data Representation project building a database to complete CRUD operations by creating and consuming RESTful APIs
    <br />
    <a href="https://github.com/colmhiggs11/Machine_Learning_21_CH"><strong>Explore the docs in Repository »</strong></a>
    <br />

</div>



<!-- TABLE OF CONTENTS -->
## Table Of Contents

1. <a href="#1-about-the-project">About The Project</a>
    - <a href="#project-description">Project Description</a>
    - <a href="#in-this-repository">In this repository</a>
2. <a href="#2-getting-started">Getting Started</a>
    - <a href="#prerequisites">Prerequisites</a>
    - <a href="#installation">Installation</a>
    - <a href="#passwords">Passwords</a>

3. <a href="#6-license">License</a>

<!-- ABOUT THE PROJECT -->
## 1. About The Project

### Project Description
Project requires a minimum of the below:
- Write a program that demonstrates that you understand creating and consuming RESTful APIs.
- Needs to consist of the following :
  - A basic Flask server
  - REST API, (to perform CRUD operations)
  - One database table
  - Accompanying web interface, using AJAX calls, to perform these CRUD operations

<p align="right">(<a href="#top">back to top</a>)</p>

### In this repository

* [README.md](https://github.com/colmhiggs11/data-representation-project/blob/main/README.md) *(Layout and details of the project)*
* [partDao.py](https://github.com/colmhiggs11/data-representation-project/blob/main/partDao.py) *(Scikit Learn Jupyter Notebook)*

* [server.py](https://github.com/colmhiggs11/data-representation-project/blob/main/server.py)  *(Scipy Stats Jupyter Notebook)*

**Other items**
* [Staticpages](https://github.com/colmhiggs11/data-representation-project/tree/main/Staticpages)
    * [index.html](https://github.com/colmhiggs11/data-representation-project/blob/main/Staticpages/index.html) *(Data File for the analysis of KNN algorithm)*
    * [login.html](https://github.com/colmhiggs11/data-representation-project/blob/main/Staticpages/login.html) *(Data file for analysis in Scikit Learn)*

* [dbconfigtemplate.py](https://github.com/colmhiggs11/data-representation-project/blob/main/dbconfigtemplate.py)
* [LICENSE](https://github.com/colmhiggs11/data-representation-project/blob/main/LICENSE) *(MIT License)*    
* [requirments.txt](https://github.com/colmhiggs11/data-representation-project/blob/main/requirements.txt)
* [initdb.sql](https://github.com/colmhiggs11/data-representation-project/blob/main/initdb.sql)
* .gitignore
<p align="right">(<a href="#top">back to top</a>)</p>

***

<!-- GETTING STARTED -->
## 2. Getting Started

This section will show how to set up the project on your local PC. At a later stage Pythonanywhere will be utilised to host the Flask server.

### **Prerequisites**

The libraries and packages that need to be installed for running this code are shown in requirements.txt, you will also need to either have access to anaconda/python and access to the browser   to work on the actual file.


### **Installation**

1. If you have anaconda installed, go to the command line and complete step 2.

2. Clone the repo
   ```sh
   git clone https://github.com/colmhiggs11/data-representation-project
   ```
3.  From here ensure all of the items in the requirments.txt file are installed. If any of them are missing or need to be updated use the following command.
    ```sh
    pip install-r requirements.txt 
    ```
4. Use the [initdb.sql](https://github.com/colmhiggs11/data-representation-project/blob/main/initdb.sql) file to set up the database and tables for App.

4. Use the [dbconfigtemplate.py](https://github.com/colmhiggs11/data-representation-project/blob/main/dbconfigtemplate.py) and edit the details to your own credentials. Also save the file as **dbcongif.py**

4. Run the server.py file as shown
   ```sh
   python server.py 
   ```
4. This will start the Flask app server at http://127.0.0.1:5000/ . Copy and Paste this url into the browser an this will open the login page for the Flask App. Passwords to progress to database page are show below. 


<p align="right">(<a href="#top">back to top</a>)</p>

### **Passwords**
The passwords below will allow the user to move from the login page into the database and perform CRUD operations on the data.

|Username|Password|
|:-------------:|:-------------:|
|colm|password|   
|admin|admin|   
|andrew|datarep|   

---

## 3.  License
This project was completed using the [MIT License](https://opensource.org/licenses/MIT). Due to the limited restrictions it puts on reuse, it has a high license compatibility.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- <https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/colmhiggs11/data-representation-project.svg?style=for-the-badge
[contributors-url]: https://github.com/colmhiggs11/data-representation-project/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/colmhiggs11/data-representation-project.svg?style=for-the-badge
[issues-url]: https://github.com/colmhiggs11/data-representation-project/issues
[license-shield]: https://img.shields.io/github/license/colmhiggs11/data-representation-project.svg?style=for-the-badge
[license-url]: https://github.com/colmhiggs11/data-representation-project/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=006
[linkedin-url]: https://linkedin.com/in/colm-higgins-3a776711b
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=006
[linkedin-url]: https://linkedin.com/in/colm-higgins-3a776711b
[product-screenshot]: images/screenshot.png
