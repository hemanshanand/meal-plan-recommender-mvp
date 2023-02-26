import streamlit as st
import pandas as pd
#change the path to your own

# Create an empty dataframe to store user profiles
user_profile_df = pd.DataFrame(columns=['user_id', 'servings', 'diet', 'food_goals'])

# Define function to get user inputs and create user profile
def get_user_profile():
    # Get number of servings
    servings = st.number_input('How many servings do you usually need?', min_value=1, max_value=15, value=4)
    
    # Get dietary requirements
    diet = ''
    if st.checkbox('Does anyone follow any diets?'):
        diet_options = ['pescatarian', 'vegetarian', 'vegan', 'pork-free', 'dairy-free', 'gluten-free']
        diet = st.multiselect('Please select dietary requirements', diet_options)

    # Get food goals
    food_goals = ''
    if st.checkbox('Does your household want to work on any of these food goals?'):
        food_goal_options = ['Eat more veg', 'Eat less meat', 'Reduce carbs', 'Lower calorie intake', 'Increase protein', 'Low fat', 'Spend less', 'Try new foods']
        food_goals = st.multiselect('Please select food goals', food_goal_options)

    # Get Cuisine details
    cuisines = ''
    cuisine_options = ['American', 'Italian', 'Mexican', 'Asian', 'Mediterranean']
    cuisines = st.multiselect('Please select cuisines', cuisine_options)

    # Create user profile
    user_profile = {'user_id': len(user_profile_df)+1, 'servings': servings, 'diet': diet, 'food_goals': food_goals, 'cuisines' : cuisines}
    
    return user_profile

# Define function to generate recipe recommendations based on user profile
def generate_recommendations(user_profile):
    # Here you can add your code to generate recommendations based on user profile
    # You can use the user_profile dictionary to filter the recipe database
    
    # As an example, we will just return some dummy recommendations
    recommendations = ['Recipe 1', 'Recipe 2', 'Recipe 3', 'Recipe 4', 'Recipe 5', 'Recipe 6']
    
    return recommendations

# Define Streamlit app
def app():
    global user_profile_df

    # Set app title
    st.title("Meal Plan Recommender System")
    
    # Get user profile
    user_profile = get_user_profile()
    
    # Save user profile to dataframe
    user_profile_df = user_profile_df.append(user_profile, ignore_index=True)
    
    # Show user profile
    # st.subheader('Your profile')
    # st.write(user_profile)
    
    # Add submit button to show recommendations
    if st.button("Submit"):
        # Generate recommendations
        recommendations = generate_recommendations(user_profile)
        
        # Show recommendations
        st.subheader('Recommendations')
        st.write(recommendations)

if __name__ == '__main__':
    app()
