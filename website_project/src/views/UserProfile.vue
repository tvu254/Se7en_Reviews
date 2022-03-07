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
        <ReviewItem     
            v-for="review in userNew.Item.reviews" 
            :key = "review.id" 
            :username = "userNew.Item.UserID" 
            :review = "review" 
            @favorite = "toggleFavorite"
        />
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
      const userNew = computed(() => store.state.User.user);
      const userId = computed(() => route.params.userId)


    // ?: get fetch to work off of mount/created. launch from there instead of follow button. --> For when Links are added to users, to redirect to a user page that isn't logged in
    // 1: Fix the genre not working so we can save the reviews to the db
    // 2: save reviews to db using POST. Send new review data from function addReview
    // 3: Figure out how backend updates db, bc we can either send whole user or just the review here
    // 4: Load these reviews into the home page as well as the browse page. 
    // 5: Add a featured review and featured songs/albums/artists to home
    // 7: Add Description / welcome message to home
    // 8: Remove the post function in user profile page without website breaking
    // 9: Add security to passwords
    // ?: Oh also figure out how props work
    // ?: Add redirects to homepage/browse when necessary (right domain, wrong extension | or review that doesnt exist, etc)
    // ?: Change userNew to user when other problem is fixed
    // ?: Output invalid username / password to user instead of just to console
    // else: Launch app as website, get user testing


      const state = reactive({
        followers: 0,
      })

      function addReview(newReviewList) {
        newReviewList[1] = newReviewList[1].charAt(0).toUpperCase() + newReviewList[1].slice(1);
        newReviewList[2] = newReviewList[2].charAt(0).toUpperCase() + newReviewList[2].slice(1);

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
          console.log(typeof(data))
          if (typeof(data) == "string") {
            console.log("invalid");   
            state.invalid = true
          }
          else
            console.log(data); 
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

    
      /*function getUsers() {
        fetch('http://localhost:5000/user/1', {
            method: "GET",

        })

        .then(resp => resp.json())
        .then(data => {

            console.log(data);
        })
        .catch(error => {
            console.log(error)      
        })
    }*/

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
        //saveReview,
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
