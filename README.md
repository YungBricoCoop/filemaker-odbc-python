# Use ODBC with Python to connect to FileMaker Database
Before using python to connect to your FileMaker database you need to follow these steps

### 1) Install the ODBC driver
Download driver : https://support.claris.com/s/article/Software-Update-FileMaker-xDBC-client-drivers-for-FileMaker-1503692806454?language=en_US

Driver Location : **C:/Users/<user>/Downloads/FileMaker Server 19.5.4/Extras/xDBC/ODBC Client Driver Installer**
Double clic on the 64 bit driver to install it. 

### 2) Enable ODBC 
Enable the ODBC/JDBC in *File -> Sharing -> Enable ODBC/JDBC*

![Pasted image 20220925124450](https://user-images.githubusercontent.com/42273436/192151086-481e4bb2-d07f-4327-98fe-fac5b9931821.png)

### 3) Change security
Add **Full Access** for **fmxdbc** in *File -> Manage -> Security -> Advanced Settings -> Extended Priviliges*

![Sans titre-1](https://user-images.githubusercontent.com/42273436/192151108-5d413c12-bef7-473f-be3c-a927d101506e.png)

### 4) ODBC Data Source
Open the **ODBC Data Source 64bit** program 

![Pasted image 20220925155219](https://user-images.githubusercontent.com/42273436/192150958-de8bae0e-e359-484f-b94b-59cbe577ea97.png)

![Pasted image 20220925155911](https://user-images.githubusercontent.com/42273436/192150981-c843f876-8935-4443-b74e-c63a2ab411da.png)

![Pasted image 20220925162655](https://user-images.githubusercontent.com/42273436/192150993-78149861-9a40-4ec2-a70b-606b4252a35c.png)

![Pasted image 20220925163321](https://user-images.githubusercontent.com/42273436/192151002-f778e597-1733-4612-999f-4666bb51c383.png)

### 5 ) Install pypyodbc
Type this into your **terminal/cmd**
```bash
pip install pypyodbc
