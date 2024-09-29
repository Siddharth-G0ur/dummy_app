import streamlit as st

def radio_button_method():
    st.header("Method 1: Radio Button Control")

    # Radio buttons for selecting active filter
    active_filter = st.radio("Select active filter:", ["Year", "Season", "Quarter"])

    # Define options for each dropdown
    year_options = list(range(2020, 2025))
    season_options = ["Spring", "Summer", "Autumn", "Winter"]
    quarter_options = ["Q1", "Q2", "Q3", "Q4"]

    # Create columns for dropdowns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Year")
        year = st.selectbox("Select Year", year_options, key="year_radio", disabled=(active_filter != "Year"))

    with col2:
        st.subheader("Season")
        season = st.selectbox("Select Season", season_options, key="season_radio", disabled=(active_filter != "Season"))

    with col3:
        st.subheader("Quarter")
        quarter = st.selectbox("Select Quarter", quarter_options, key="quarter_radio", disabled=(active_filter != "Quarter"))

    # Display selected values
    st.write(f"Selected Year: {year}")
    st.write(f"Selected Season: {season}")
    st.write(f"Selected Quarter: {quarter}")

def mutually_exclusive_method():
    st.header("Method 2: Mutually Exclusive Filters")

    # Define options for each dropdown
    year_options = ["None"] + list(range(2020, 2025))
    season_options = ["None", "Spring", "Summer", "Autumn", "Winter"]
    quarter_options = ["None", "Q1", "Q2", "Q3", "Q4"]

    # Initialize session state for selected values
    if 'active_filter' not in st.session_state:
        st.session_state.active_filter = None
    if 'year_me' not in st.session_state:
        st.session_state.year_me = "None"
    if 'season_me' not in st.session_state:
        st.session_state.season_me = "None"
    if 'quarter_me' not in st.session_state:
        st.session_state.quarter_me = "None"

    # Function to update selected value and reset others
    def update_selection(filter_name):
        value = getattr(st.session_state, f"{filter_name}_select")
        if value != "None":
            st.session_state.active_filter = filter_name
            for other in ['year_me', 'season_me', 'quarter_me']:
                if other != filter_name:
                    setattr(st.session_state, other, "None")
        else:
            st.session_state.active_filter = None
        setattr(st.session_state, filter_name, value)

    # Create columns for dropdowns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Year")
        year = st.selectbox("Select Year", year_options, key="year_me_select",
                            disabled=(st.session_state.active_filter is not None and st.session_state.active_filter != 'year_me'),
                            on_change=update_selection, args=('year_me',))

    with col2:
        st.subheader("Season")
        season = st.selectbox("Select Season", season_options, key="season_me_select",
                              disabled=(st.session_state.active_filter is not None and st.session_state.active_filter != 'season_me'),
                              on_change=update_selection, args=('season_me',))

    with col3:
        st.subheader("Quarter")
        quarter = st.selectbox("Select Quarter", quarter_options, key="quarter_me_select",
                               disabled=(st.session_state.active_filter is not None and st.session_state.active_filter != 'quarter_me'),
                               on_change=update_selection, args=('quarter_me',))

    # Display selected values
    st.write(f"Selected Year: {st.session_state.year_me}")
    st.write(f"Selected Season: {st.session_state.season_me}")
    st.write(f"Selected Quarter: {st.session_state.quarter_me}")
    
def main():
    st.title("Filter Methods Comparison")

    radio_button_method()
    
    st.markdown("---")  # Add a horizontal line for separation
    
    mutually_exclusive_method()

if __name__ == "__main__":
    main()