<template>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <CreateReviewPanel @add-review="addReview"/>
    </div>
    <div class = "userReviewsWrapper">
        <div class = "reviewName">
            @{{userNew.Item.UserID}}'s Reviews:
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
  components: { CreateReviewPanel, ReviewItem },
  setup() {

      const store = useStore();
      const route = useRoute();
      const router = useRouter();
      const userNew = computed(() => store.state.User.user);
      const userId = computed(() => route.params.userId)


    // 1: get fetch to work off of mount/created. launch from there instead of follow button. --> This is for loading a profile when clicked, while this .vue is for clicking on own profile
    // 3: save reviews to db using POST. Send new review data from function addReview
    // 4: Figure out how backend updates db, bc we can either send whole user or just the review here

      const state = reactive({
        followers: 0,
      })

      function addReview(newReviewList) {
        newReviewList[1] = newReviewList[1].charAt(0).toUpperCase() + newReviewList[1].slice(1);

        userNew.value.Item.reviews.unshift( {
            id: userNew.value.Item.reviews.length + 1,
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
