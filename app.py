import streamlit as st
import pandas as pd



# Create a function for the policy search dashboard
def policy_search():
   

    # Load data
    @st.cache_data
    def load_data():
        data = pd.read_csv('fullpolicylist.csv')  
        return data

    data = load_data()
    
    st.markdown(
        """
        <style>
            body {
                background-color: #D67B82; /* Pink */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Policy Search 🔍")

    st.sidebar.header("Filter options")

    # Select State
    state = st.sidebar.selectbox('Select State', options=data['State'].unique())

    # Select Year using a dropdown menu
    year = st.sidebar.selectbox('Select Year', options=data['Year'].unique())
    
     # Create a link to the landing page
    landing_page_link = "[Back to Landing Page](https://clever-state-2zd5.figment.so/)"
    st.sidebar.markdown(landing_page_link, unsafe_allow_html=True)
    

    filtered_data = data[(data['State'] == state) & (data['Year'] == year)]

    if not filtered_data.empty:
        st.dataframe(filtered_data.style.format({"Year": "{:}"}))
    else:
        st.write("No policies found for the selected criteria.")

# Main function to decide which page to show based on user input
def main():
  
  policy_search()

if __name__ == "__main__":
    main()
