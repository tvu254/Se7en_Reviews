<template>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <div class = "userProfilePanel">
            <h1 class = "userProfileUsername">{{ state.user.firstName }} {{ state.user.lastName }}  -  @{{ state.user.username }}</h1>
            <h2> User ID: {{ userId }}</h2>
            <div class = "verifiedBadge" v-if="state.user.isVerified">
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
            @{{state.user.username}}'s Reviews:
        </div> 
        <ReviewItem 
            v-for="review in state.user.reviews" 
            :key = "review.id" 
            :username = "state.user.username" 
            :review = "review" 
            @favorite = "toggleFavorite"
        />
    </div>
        <div class = "followButton">
            <button v-on:click="followUser">
                Follow
            </button>
        </div>
    </div>
</template>

<script>
import { reactive, watch, computed } from 'vue';
import { useRoute } from 'vue-router';
import { users } from "../assets/users";
import ReviewItem from "../components/ReviewItem.vue"
import CreateReviewPanel from "../components/CreateReviewPanel.vue";

export default {
  name: 'UserProfile',
  components: { CreateReviewPanel, ReviewItem },
  setup() {

      const route = useRoute();
      const userId = computed(() => route.params.userId)

    // if userId exists, get user from db, store like below
    // make 'users' below a js object and store its data. should be able to reference it just like I do below
    // STATE HOLDS THE CURRENT STATE SET IN ROUTER (will be register/login) BUT STILL CALLS THE USER DECLARED BELOW LIKE state.user. => so all is well lol
    // 1: get fetch to work off of mount/created. launch from there instead of follow button.
    // 2: store returned data into user variable below. Everything should work the same if stored correctly.
    // 3: save reviews to db using POST. Send new review data from function addReview
    // 4: Figure out how backend updates db, bc we can either send whole user or just the review here
    // 5: Once that works, get started on login/register and maintaining state

      const state = reactive({
        followers: 0,
        user: users[userId.value - 1] || users[0]       // this line gets the user from users.js instead of db, should have getUsers in here instead
      })

      function addReview(newReviewList) {
        newReviewList[1] = newReviewList[1].charAt(0).toUpperCase() + newReviewList[1].slice(1);

        state.user.reviews.unshift( {
            id: state.user.reviews.length + 1,
            type: newReviewList[1],
            genre: 'WIP',
            content: newReviewList[0]
        });
    }

      function toggleFavorite(id) {
        console.log(`Favorited Review = ${id}`)
    }

      function followUser() {
        state.followers++
        getUsers() // should be on created
        console.log("data");
    }

    
      function getUsers() {
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
