import pickle
import streamlit as st
import sklearn

# Comparing the original model results to the pickled model
model = pickle.load(open('model.pkl','rb'))
# print(model.predict(X_test) == y_pred)


st.title("Magic Box Office Predictor App")
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
ratings = ["G", "PG", "PG-13", "R", "NC-17", "Unrated"]
genres = sorted(['Action', 'Adventure', 'Drama', 'Sci-Fi',
          'Animation', 'Family', 'Musical', 'Comedy', 'Fantasy', 'Romance',
          'Crime', 'Thriller', 'Horror', 'Mystery', 'Biography', 'Sport', 'Music',
          'History', 'War', 'Documentary', 'Western', 'Short', 'News'])

title_st = "blank"
producer_st = "blank"
year_st = "blank"
runtime_st = "blank"

title_st = st.text_input("What is the name of your movie?")
year_st = st.selectbox("Choose Release Year, past or present", options=years)
month_st = st.selectbox("Choose your release month", options = months)
producer_st = st.text_input("Who is producing your film?")
big_six_st = st.checkbox("Is this producer one of the 'big six' \n "
                         "(20th Century Fox/WarnerBros./Universal/Disney/Paramount/Sony)")
black_list_st = st.checkbox("Did your script appear on the Hollywood 'Blacklist' of promising scripts?")
runtime_st = st.slider("How long is your film going to be? (minutes)", 1, 300)
days_st = st.slider("How many days do you expect to have your film in theaters?", 1, 500 )
theaters_st = st.slider("How many theaters will you have the film in?", 1, 4000)
rating_st = st.selectbox("What will your film be rated?", options = ratings)
genres_st = st.multiselect("Choose your film's genre(s)", options=genres)

# Magic functions that will help build out my end array

def month_machine(month):
    global months

    ending_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i,m in enumerate(months):
        if m == month:
            ending_list[i] = 1

    return ending_list


def rating_machine(rating):
    global ratings

    ending_list = [0, 0, 0, 0, 0, 0]

    for i, r in enumerate(ratings):
        if r == rating:
            ending_list[i] = 1

    return ending_list


def genre_machine(selected_genre):
    global genres

    ending_list = []

    for i in range(0, len(genres)):
        ending_list.append(0)

    for i, g in enumerate(genres):
        if g in selected_genre:
            ending_list[i] = 1

    return ending_list

array_st = [year_st, runtime_st, days_st, theaters_st, int(black_list_st), int(big_six_st)]
array_st.extend(rating_machine(rating_st))
array_st.extend(month_machine(month_st))
array_st.extend(genre_machine(genres_st))
#final_list = []
# final_list.append(array_st)

predicted_gross = model.predict([array_st])

st.write(f"Looking into my magic crystal ball, I predict that {title_st} will make (or would have made)"
         f" ${round(predicted_gross[0]):,} at the box office!")

# This is for internal testing
# st.write(f"Your movie title: {title_st}")
# st.write(f"Your release year: {year_st}")
# st.write(f"Your release month: {month_st}")
# st.write(f"Your producer: {producer_st}")
# st.write(f"Your film's runtime: {runtime_st} minute(s)")
# st.write(f"Your film will be in theaters for {days_st} day(s)")
# st.write(f"Your film will be in {theaters_st} theater(s)")
# st.write(f"Your film's rating: {rating_st}")
# st.write(f"Your film's genre(s): {genres_st}")
