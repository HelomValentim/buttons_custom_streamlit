import streamlit as st

def btn_blue(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Blue
        
        Creates a custom-styled blue button while preserving all functionality of `st.button`.

        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.

    """
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
    if st.button(        
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_blue_nbg(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Blue No Background
        
        Creates a custom-styled blue button with no background while preserving all functionality of `st.button`.
            
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
        
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_orange(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Orange
        
        Creates a custom-styled orange button while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_orange_nbg(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Orange No Background
        
        Creates a custom-styled orange button with no background while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_green(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Green
        
        Creates a custom-styled green button while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
    
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_green_nbg(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Green No Background
        
        Creates a custom-styled green button with no background while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
        """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_red(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Red
        
        Creates a custom-styled red button while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
    
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_red_nbg(
    label: str,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Red No Background
        
        Creates a custom-styled red button with no background while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True

def btn_style(
    label: str,
    txtColor: str,
    bgColor: str = None,
    hoverTxtColor: str = None,
    hoverBgColor: str = None,
    key: str = None,
    help: str = None,
    on_click=None,
    args=(),
    kwargs={},
    disabled: bool = False,
    use_container_width: bool = False
):
    r"""
        Styled Button - Custom Colors
        
        Creates a custom-styled button with custom text and background colors while preserving all functionality of `st.button`.
        
        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
            The label can optionally contain GitHub-flavored Markdown of the
            following types: Bold, Italics, Strikethroughs, Inline Code, Links,
            and Images. Images display like icons, with a max height equal to
            the font height.
        
        txtColor : str
            The color of the button text. Accepts any valid CSS color value.
            
        bgColor : str
            The color of the button background. Accepts any valid CSS color value.
            If ``bgColor`` is ``None`` (default), the button will have no background.
        
        hoverTxtColor : str
            The color of the button text when hovered over. Accepts any valid CSS color value.
            If ``hoverTxtColor`` is ``None`` (default), the text color will change to white.
        
        hoverBgColor : str
            The color of the button background when hovered over. Accepts any valid CSS color value.
            If ``hoverBgColor`` is ``None`` (default), the background color will change to the text color.

        key : str or int
            An optional string or integer to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. No two widgets may have the same key.
        help : str
            An optional tooltip that gets displayed when the button is
            hovered over.

        on_click : callable
            An optional callback invoked when this button is clicked.

        args : tuple
            An optional tuple of args to pass to the callback.

        kwargs : dict
            An optional dict of kwargs to pass to the callback.

        icon : str or None
            An optional emoji or icon to display next to the button label. If ``icon``
            is ``None`` (default), no icon is displayed. If ``icon`` is a
            string, the following options are valid:

            - A single-character emoji. For example, you can set ``icon="🚨"``
              or ``icon="🔥"``. Emoji short codes are not supported.

            - An icon from the Material Symbols library (rounded style) in the
              format ``":material/icon_name:"`` where "icon_name" is the name
              of the icon in snake case.

              For example, ``icon=":material/thumb_up:"`` will display the
              Thumb Up icon. Find additional icons in the `Material Symbols \
              <https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded>`_
              font library.

        disabled : bool
            An optional boolean that disables the button if set to ``True``.
            The default is ``False``.

        use_container_width : bool
            Whether to expand the button's width to fill its parent container.
            If ``use_container_width`` is ``False`` (default), Streamlit sizes
            the button to fit its contents. If ``use_container_width`` is
            ``True``, the width of the button matches its parent container.

            In both cases, if the contents of the button are wider than the
            parent container, the contents will line wrap.

        Returns
        -------
        bool
            True if the button was clicked on the last run of the app,
            False otherwise.
        
        Example
        -------
        >>> import streamlit as st
        >>> from styled_components import btn_style
        ...
        >>> if btn_style('Click Me', txtColor='black', bgColor='red', hoverTxtColor='white', hoverBgColor='black', key='btn_black_red'):
        >>>     st.write('Button Clicked!')
        ...
    """
    
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
    if st.button(
        label,
        key=key,
        help=help,
        on_click=on_click,
        args=args,
        kwargs=kwargs,
        disabled=disabled,
        use_container_width=use_container_width
        ):
        return True
    return False
