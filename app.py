import streamlit as st
import pandas as pd

def policy_search():

    @st.cache_data
    def load_data():
        # Load policy data
        data = pd.read_csv('fullpolicylist.csv')
        data['full_policy'] = data['full_policy'].str.strip()

        # Load ML model predictions
        predictions = pd.read_csv('final_data.csv')

        return data, predictions

    data, predictions = load_data()

    st.title("Policy Search 🔍")
    st.sidebar.header("Filter options")

    state = st.sidebar.selectbox('Select State', options=data['State'].unique())
    
    sorted_years = sorted(data['Year'].unique())
    year = st.sidebar.selectbox('Select Year', options=sorted_years)
    

    landing_page_link = "[Back to Landing Page](https://clever-state-2zd5.figment.so/)"
    st.sidebar.markdown(landing_page_link, unsafe_allow_html=True)

    filtered_data = data[(data['State'] == state) & (data['Year'] == year)]
    
    if not filtered_data.empty:
        st.dataframe(filtered_data.style.format({"Year": "{:}"}))

        # Display ML model predictions if available
        prediction_row = predictions[(predictions['State'] == state) & (predictions['Year'] == year)]
        if not prediction_row.empty:
            impact_direction = "increase" if prediction_row['predicted_DiD_rate_for_women'].item() > 0 else "decrease"
            st.write(f"This policy, enacted in {prediction_row['Year'].item()}, is associated with a "
                     f"{impact_direction} in the abortion rate by "
                     f"{abs(prediction_row['predicted_DiD_rate_for_women'].item()):.2f} percentage points. "
                     "The figure is estimated from a model using historical policy data to understand "
                     "potential impacts. As actual data becomes available, the true impact of this policy "
                     "will be more accurately determined and may differ from this initial prediction.")
        else:
            st.write("No predictions found for the selected criteria.")
    else:
        st.write("No policies found for the selected criteria.")

def main():
    policy_search()

if __name__ == "__main__":
    main()
