<template>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <div class = "userProfilePanel">
            <h1 class = "userProfileUsername">{{ state.firstName }} {{ state.lastName }}</h1>
            <h1> &nbsp; AKA </h1>
            <h1> {{ userId }} </h1>
            <div class = "verifiedBadge" v-if="state.isVerified">
                Verified
            </div>
            <br>
            <div class = "userProfileData">
                <strong> Followers: </strong> {{ state.followers }}
                <br>
                <strong> Likes: </strong> {{ state.likes }}
                <br>
                <strong> Average Rating: </strong> {{ state.averageRating }}
                <br>
                <strong> Review Count: </strong> {{ state.reviews.length }}
            </div>
        </div>

    </div>
    <div class = "userReviewsWrapper">
        <div class = "reviewName">
            {{state.UserID}}'s Reviews:
        </div> 

        <div v-if="state.reviews.length != 0">
          <ReviewItem     
              v-for="review in state.reviews" 
              :key = "review.id" 
              :username = "state.UserID" 
              :loggedIn = "false"
              :review = "review" 
              @favorite = "toggleFavorite"
          />
        </div>
        <div v-else> Nothing yet :)</div>

      </div>
    </div>
</template>

<script>
// will currently take to current users page if logged in
import { reactive, watch, computed } from 'vue';
import { useRoute } from 'vue-router';
import ReviewItem from "../components/ReviewItem.vue"

export default {
  name: 'Profile',
  components: { ReviewItem },    // the emit from userReviews probably making it to where i cant remove createReviewPanel
  setup() {
      const route = useRoute();
      const userId = computed(() => route.params.userId)


        // fetch user, set to user in state
        const data = {
          username: userId.value,
          password: 'sgdfsd5897jds5hd3h3dfs56h4dhj56d4h756d545hftdh'
        };

        fetch('http://localhost:5000/login', {
          method: 'POST',
          body: JSON.stringify({ data }),
          headers: {
            'Content-type': 'application/json',
          }
        })
        .then((response) => response.json())
        .then(function (data) {
          console.log(data)
          if (data == "Invalid Password") {
            console.log("invalid username or password");
            state.invalid = true   
          }
          else if (data == "Failed to find user") {
            console.log("user not found")
          }
          else if (data == "Something went horribly wrong") {
            console.log("Something went horribly wrong")
          }
          else 
            setProfile(data);
        })
        .catch(function (error) {
          console.warn('Something went horribly wrong.', error);
        });

      const setProfile = async (user) => {
        state.firstName = user.Item.firstName;
        state.lastName = user.Item.lastName;
        state.isVerified = user.Item.isVerified
        state.UserID = user.Item.UserID
        state.reviews = user.Item.reviews
        state.likes = 0
        state.averageRating = "N/A"
      }

      const state = reactive({
        followers: 0,
        firstName: '',
        lastName: '',
        isVerified: false,
        UserID: '',
        likes: 0,
        averageRating: "N/A",
        reviews: []
      })

      function toggleFavorite(id) {
        console.log(`Favorited Review = ${id}`)
    }


      watch(() => state.followers, (followers, oldFollowerCount) => { 
        if (oldFollowerCount < followers) {
        console.log(`${state.UserID} has gained a follower`)
        }
      })

    return {
        state,
        toggleFavorite,
        userId,
        setProfile
    }
  },
}
</script>

<style lang="scss" scoped>

@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');
 
.userProfile {
    display: grid;
    grid-template-columns: 1fr 3fr;
    grid-gap: 50px;
    padding: 50px 5%;

    .userProfilePanel {
        display: flex;
        flex-direction: column;
        padding: 20px;
        background-color: #ececec;
        border-radius: 5px;
        border: 1px solid #0d1424;

        h1 {
            margin: 0;
            font-size: 28px;
        }

        .verifiedBadge {
            background: rgb(153, 20, 170);
            color: white;
            border-radius: 5px;
            margin-right: auto;
            padding: 0 10px;
            font-weight: bold;
            margin-top: 5px;
            margin-bottom: 5px;
        }
    }
}

.followButton {
    text-align: center;
}

.logoutButton {
    text-align: center;
    cursor: pointer;        // doesnt work, only on outside

    &:hover {
        transform: scale(1.1, 1.1);
      }
}

.userReviewsWrapper {
    display: grid;
    grid-gap: 10px;
    text-align: center;
    margin-top: 5px;
    color: #0d1424;
    font-size: 16px;

    .reviewName {
        font-size: 20px;
        font-weight: bold;
    }
}


</style>
