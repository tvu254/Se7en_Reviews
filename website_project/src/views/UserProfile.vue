<template>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <div class = "userProfilePanel">
            <h1 class = "userProfileUsername">{{ userNew.Item.firstName }} {{ userNew.Item.lastName }}</h1>
            <h1> &nbsp; AKA </h1>
            <h1> {{ userId }} </h1>
            <div class = "verifiedBadge" v-if="userNew.Item.isVerified">
                Verified
            </div>
            <div class = "userProfileFollowerCt">
                <strong> Followers: </strong> {{ state.followers }}
            </div>
        </div>
        <CreateReviewPanel @add-review="addReview"/>
    </div>
    <div class = "userReviewsWrapper">
        <div class = "reviewName">
            {{userNew.Item.UserID}}'s Reviews:
        </div> 

        <div v-if="userNew.Item.reviews.length != 0">
          <ReviewItem     
              v-for="review in userNew.Item.reviews" 
              :key = "review.id" 
              :username = "userNew.Item.UserID" 
              :review = "review" 
              @favorite = "toggleFavorite"
          />
        </div>
        <div v-else> Nothing yet :)</div>

    </div>
        <div class = "followButton">
            <button v-on:click="followUser">
                Follow
            </button>
        </div>
        <div class = "logoutButton">
            <button v-on:click="logout">
                Logout
            </button>
        </div>
    </div>
</template>

<script>
import { reactive, watch, computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute, useRouter } from 'vue-router';
import ReviewItem from "../components/ReviewItem.vue"
import CreateReviewPanel from "../components/CreateReviewPanel.vue";

export default {
  name: 'UserProfile',
  components: { CreateReviewPanel, ReviewItem },    // the emit from userReviews probably making it to where i cant remove createReviewPanel
  setup() {

      const store = useStore();
      const route = useRoute();
      const router = useRouter();
      const userId = computed(() => route.params.userId)
      const userNew = computed(() => store.state.User.user);
      if(userNew.value == null) {
        // fetch user, set to userNew
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
            console.log(data);  
            // FIXME: STILL sets the user // figure out how the data is called and make it work throughout
            setUser(data);
        })
        .catch(function (error) {
          console.warn('Something went horribly wrong.', error);
        });
      }

      const setUser = async (user) => {
        await store.dispatch('User/setUser', user);
        console.log(user.Item.username)
        await router.push('/');
      }

    // ?: when Links are added to users, to redirect to a user page that isn't logged in
    // 4: Load these reviews into the home page as well as the browse page, in some meaningful order/way
    // 4.20: add links to the users names that direct to their page. clicking on the review expands it. For when we have more info there
    // 5.5: Might need to have a date created in the review data, as well as account creation date
    // 5.6: Add stats to user like average rating, past likes, total likes, etc. I think we should remove followers and just have average review rating and number of ratings. That way famous people's opinions wouldnt be more important
    // 6: add artist, album, songname to review
    // 8: Remove the post function in user profile page without website breaking
    // 9: Add security to passwords
    // ?: Add redirects to homepage/browse when necessary (right domain, wrong extension | or review that doesnt exist, etc)
    // ?: Change userNew to user when other problem is fixed
    // ?: Be able to edit specific values of your review - could be added as a separate page, linked to by both profile and post
    // ?: Add click outside functionality for dropdown boxes
    // ?: Order the reviews in reverse-id order so the newest is at front
    // else: Launch app as website, get user testing

    // BY PRESENTATION DAY
    // links of reviewers take you to profile
    // post panel removed from user page
    // add date created to reviews and profiles
    // add adding song, artist, album to review
    // delete/edit review
    //    ^--> this requires a drop-down box when clicking review. Asks for edit or delete. Edit will have to be it's own component. Data sent to flask will replace every value in current review, then entered. Delete asks if you are sure  
    // register name updates

      const state = reactive({
        followers: 0,
        reviews: userNew.value.Item.reviews
        

      })

      function addReview(newReviewList) {
        // capitalizes the first letter for equivalence
        newReviewList[1] = newReviewList[1].charAt(0).toUpperCase() + newReviewList[1].slice(1);
        newReviewList[2] = newReviewList[2].charAt(0).toUpperCase() + newReviewList[2].slice(1);

        // add review to local user, then call save
        userNew.value.Item.reviews.unshift( {
            id: userNew.value.Item.reviews.length + 1,
            type: newReviewList[1],
            genre: newReviewList[2],
            content: newReviewList[0]
        });
        saveReview([userNew.value.Item.reviews[0], userNew.value.Item.UserID])
    }


      const saveReview = async (review) => {
        
        await fetch('http://localhost:5000/post', {
          method: 'POST',
          body: JSON.stringify({ review }),
          headers: {
            'Content-type': 'application/json',
          }
        })
        .then((response) => response.json())
        .then(function (data) {
          console.log(data)             // flask returns a response object
        })
        .catch(function (error) {
          console.warn('Something went horribly wrong.', error);
        });
      };

      function toggleFavorite(id) {
        console.log(`Favorited Review = ${id}`)
    }

      function followUser() {
        state.followers++
        //getUsers() // should be on created
        console.log("data");
    }

      const logout = async () => {
        await store.dispatch('User/setUser', null);
        await router.push('/');
      }

      watch(() => state.followers, (followers, oldFollowerCount) => { 
        if (oldFollowerCount < followers) {
        console.log(`${state.user.username} has gained a follower`)
        }
      })

    return {
        state,
        addReview,
        toggleFavorite,
        followUser,
        userId,
        logout,
        userNew
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
