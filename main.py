# ----- intro -----

"""

main running file for code49's personal website.
hydralit/streamlit will run from here, pulling code for other pages from files.

"""

# ----- import add-on libraries -----

import streamlit as st
import hydralit as hy
import hydralit_components as hc

# ----- import other files -----

from footer import renderFooter

# ----- code -----

if __name__ == '__main__':

    # --- setup streamlit, hydralit, hydralit navbar ---

    # setup streamlit page configuration
    st.set_page_config(
        page_title="david chan",
        page_icon="🚋",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    # create hydralit app
    app = hy.HydraApp(

        # page title/favicon
        title="david chan",
        favicon="🔺",
        
        # theme configuration
        navbar_theme={
            'txc_inactive': '#FFFFFF',
            'menu_background':'#C20101',
            'txc_active':'#000000',
            'option_active':'#F7F7F7'
        },

        # setting configuration
        allow_url_nav=True,
        sidebar_state="collapsed",
        clear_cross_app_sessions=True,
        hide_streamlit_markers=True,
        use_navbar=True,
        navbar_animation=False,
        navbar_sticky=True
    )

    # --- setup hydralit paging ---

    # - wrapper class imports - 

    # about
    from about.about import RenderAboutPage

    # education
    from education.classnotes import RenderClassnotesPage
    from education.cmu import RenderCarnegiePage
    from education.nueva import RenderNuevaPage

    # experience
    from experience.projects import RenderProjectsPage
    from experience.resume import RenderResumePage
    from experience.tau import RenderTauPage
    from experience.ucsf_bchsi import RenderUCSFBakarPage
    from experience.vestaboard import RenderVestaboardPage

    # home page
    from homepage.homepage import RenderHomePage

    # - add sub-pages as apps to the main app -

    # home
    app.add_app(
        title="home 🏠",
        app=RenderHomePage()
    )

    # experience
    app.add_app(
        title="projects",
        app=RenderProjectsPage()
    )
    
    app.add_app(
        title="resume",
        app=RenderResumePage()
    )

    app.add_app(
        title="tau",
        app=RenderTauPage()
    )

    app.add_app(
        title="ucsf bakar",
        app=RenderUCSFBakarPage()
    )

    app.add_app(
        title="vestaboard",
        app=RenderVestaboardPage()
    )

    # education
    app.add_app(
        title="classnotes",
        app=RenderClassnotesPage()
    )

    app.add_app(
        title="nueva",
        app=RenderNuevaPage()
    )

    app.add_app(
        title="carnegie mellon",
        app=RenderCarnegiePage()
    )

    # about
    app.add_app(
        title="about 👨‍💻",
        app=RenderAboutPage()
    )

    complex_nav = {
        "home": ["home 🏠"],
        "experience 🌄": ["resume", "tau", "vestaboard", "ucsf bakar", "projects"],
        "education ✏️": ["carnegie mellon", "nueva", "classnotes"],
        "about": ["about 👨‍💻"]
    }

    # show navbar + app content
    app.run(complex_nav)

    # show footer
    renderFooter()
