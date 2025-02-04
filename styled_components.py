import streamlit as st

def btn_blue(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_blue {
            display: none;
        }
        .element-container:has(#button-after_blue) {
            display: none;
        }
        .element-container:has(#button-after_blue) + div button {
            background-color: #1a17d1;
            color: white !important;
            border-radius: 7px;
            border: none;
            cursor: pointer;
            }
        .element-container:has(#button-after_blue) + div button:hover {
            background-color: #110f91;
            color: white !important;
            border: 1px solid #1a17d1;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_blue"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_blue_nbg(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_blue_nbg {
            display: none;
        }
        .element-container:has(#button-after_blue_nbg) {
            display: none;
        }
        .element-container:has(#button-after_blue_nbg) + div button {
            color: #1a17d1 !important;
            border: 1px solid #1a17d1;
            border-radius: 7px;
            cursor: pointer;
            }
        .element-container:has(#button-after_blue_nbg) + div button:hover {
            color: white !important;
            background-color: #1a17d1;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_blue_nbg"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_orange(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_orange {
            display: none;
        }
        .element-container:has(#button-after_orange) {
            display: none;
        }
        .element-container:has(#button-after_orange) + div button {
            background-color: #FFA500;
            color: white !important;
            border-radius: 7px;
            border: none;
            cursor: pointer;
            }
        .element-container:has(#button-after_orange) + div button:hover {
            background-color: #CC8400;
            color: white !important;
            border: 1px solid #FFA500;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_orange"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_orange_nbg(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_orange_nbg {
            display: none;
        }
        .element-container:has(#button-after_orange_nbg) {
            display: none;
        }
        .element-container:has(#button-after_orange_nbg) + div button {
            color: #FFA500 !important;
            border: 1px solid #FFA500;
            border-radius: 7px;
            cursor: pointer;
            }
        .element-container:has(#button-after_orange_nbg) + div button:hover {
            color: white !important;
            background-color: #FFA500;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_orange_nbg"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_green(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_green {
            display: none;
        }
        .element-container:has(#button-after_green) {
            display: none;
        }
        .element-container:has(#button-after_green) + div button {
            background-color: #1da10b;
            color: white !important;
            border-radius: 7px;
            border: none;
            cursor: pointer;
            }
        .element-container:has(#button-after_green) + div button:hover {
            background-color: #146908;
            color: white !important;
            border: 1px solid #1da10b;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_green"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_green_nbg(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_green_nbg {
            display: none;
        }
        .element-container:has(#button-after_green_nbg) {
            display: none;
        }
        .element-container:has(#button-after_green_nbg) + div button {
            color: #1da10b !important;
            border: 1px solid #1da10b;
            border-radius: 7px;
            cursor: pointer;
            }
        .element-container:has(#button-after_green_nbg) + div button:hover {
            color: white !important;
            background-color: #1da10b;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_green_nbg"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_red(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_red {
            display: none;
        }
        .element-container:has(#button-after_red) {
            display: none;
        }
        .element-container:has(#button-after_red) + div button {
            background-color: #ff0000;
            color: white !important;
            border-radius: 7px;
            border: none;
            cursor: pointer;
            }
        .element-container:has(#button-after_red) + div button:hover {
            background-color: #cc0000;
            color: white !important;
            border: 1px solid #ff0000;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_red"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_red_nbg(label):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after_red_nbg {
            display: none;
        }
        .element-container:has(#button-after_red_nbg) {
            display: none;
        }
        .element-container:has(#button-after_red_nbg) + div button {
            color: #ff0000 !important;
            border: 1px solid #ff0000;
            border-radius: 7px;
            cursor: pointer;
            }
        .element-container:has(#button-after_red_nbg) + div button:hover {
            color: white !important;
            background-color: #ff0000;
            
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after_red_nbg"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True

def btn_style(label, txtColor, bgColor: str = None, hoverTxtColor: str = None,hoverBgColor: str = None):
    text = f"""
    <style>
    .element-container:has(style) {{
        display: none;
    }}
    #button-after_style {{
        display: none;
    }}
    .element-container:has(#button-after_style) {{
        display: none;
    }}
    .element-container:has(#button-after_style) + div button {{
        background-color: {bgColor};
        color: {txtColor} !important;
        border-radius: 7px;
        border: 1px solid {txtColor};
        cursor: pointer;
    }}
    .element-container:has(#button-after_style) + div button:hover {{
        background-color: {hoverBgColor if hoverBgColor != None else txtColor};
        color: {hoverTxtColor if hoverTxtColor != None else 'white'} !important;
        # border: 1px solid {bgColor};
    }}
    </style>
    """
    st.markdown(text, unsafe_allow_html=True)
    st.markdown(f'<span id="button-after_style"></span>', unsafe_allow_html=True)
    if st.button(label):
        return True
    return False