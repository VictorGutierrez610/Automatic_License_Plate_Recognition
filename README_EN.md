# Automatic License Plate Recognition System for Garage Door Control

This project aims to build an **automatic license plate recognition system** to open a garage door for authorized vehicles. The system uses **Azure's Optical Character Recognition (OCR)**, **Python** for processing, and a **database** to manage the list of authorized license plates.

## Project Overview

The goal is to create a seamless and automated system that can:
- Recognize license plates from incoming vehicles.
- Cross-check the detected license plate with a database of authorized vehicles.
- Automatically open the garage door for authorized vehicles.

## Technologies

- **Azure OCR API**: To accurately detect and extract the license plate number from images.
- **Python**: To manage image processing and system logic, using libraries like OpenCV for image manipulation and interaction with the Azure OCR API.
- **Database (SQL)**: A database to store and manage the authorized license plates. This will allow for quick verification and flexibility in updating the list of vehicles allowed entry.
- **Raspberry Pi** (Optional): If you want to integrate hardware for the control of the garage door.

## Steps to Develop the Project

1. **Camera Setup**: 
   - Install a camera to capture images of approaching vehicles. This could be a USB camera or an IP camera.
   
2. **Image Processing and Plate Detection**: 
   - Use **OpenCV** in Python to process the captured images and isolate the license plate area. This includes applying filters, detecting edges, and extracting the license plate region.

3. **License Plate Recognition**: 
   - Use **Azure OCR** to extract the text from the processed license plate image. The OCR API will convert the image of the license plate into readable text.

4. **Database for Verification**:
   - Create a **SQL database** to store the list of authorized license plates. Each time a plate is detected, the system will query this database to check whether the vehicle is authorized.

5. **Automated Garage Door Control**: 
   - If the vehicle is authorized, a signal will be sent to the garage door control system to open it automatically.

6. **User Interface (Optional)**: 
   - Develop a simple web interface to manage the authorized vehicle list, allowing users to add, edit, or delete entries from the database.

## Future Features

- **Real-time Notifications**: Receive alerts for unauthorized access attempts.
- **Access Logs**: Keep a record of all vehicle entries and exits for future analysis.
- **Machine Learning Integration**: Improve the system's ability to recognize obscure or partially hidden plates using machine learning models.

## Final Thoughts

This project will help me delve deeper into areas like **computer vision**, **cloud-based OCR solutions**, and **database management**, all while creating a practical and useful system. It demonstrates how AI can be applied to everyday automation challenges.
