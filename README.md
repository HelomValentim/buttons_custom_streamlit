# Custom Buttons for Streamlit

This repository provides a collection of custom-styled buttons for Streamlit applications. These buttons allow users to enhance the appearance of their Streamlit UI with various colors and hover effects.

## Features

- **Predefined Colors**: Blue, Orange, Green, and Red buttons.
- **No Background Variants**: Transparent background with colored borders.
- **Customizable Button**: Define your own colors for text, background, and hover effects.

## Installation

Ensure you have Streamlit installed:

```sh
pip install streamlit
```

## Usage

Import the functions and use them in your Streamlit app. All custom button functions maintain the same parameters as ```python st.button: ```

```python
import streamlit as st
from custom_buttons import btn_blue, btn_orange, btn_green, btn_red, btn_style

if btn_blue("Blue Button", key="btn1"):
    st.write("Blue button clicked!")

if btn_style("Custom Button", txtColor="#FFFFFF", bgColor="#000000", hoverBgColor="#555555"):
    st.write("Custom button clicked!")
```

## Screenshot

![image](https://github.com/user-attachments/assets/5a958b2b-fc75-4d9f-a92f-7c6600f293b2)

## License

This project is licensed under the MIT License.



