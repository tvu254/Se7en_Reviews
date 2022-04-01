<template>
  <Profile v-if="state.notLoggedIn || ((state.UserID != state.userTestVal))"/>
  <div v-else>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <div class = "userProfilePanel">
            <h1 class = "userProfileUsername">{{ user.Item.firstName }} {{ user.Item.lastName }}</h1>
            <h1> &nbsp; AKA </h1>
            <h1> {{ userId }} </h1>
            <div class = "verifiedBadge" v-if="user.Item.isVerified">
                Verified
            </div>
            <div class = "userProfileData">
                <br>
                <strong> Followers: </strong> {{ state.followers }}
                <br>
                <strong> Likes: </strong> 0
                <br>
                <strong> Average Rating: </strong> N/A
                <br>
                <strong> Review Count: </strong> {{ user.Item.reviews.length }}
            </div>
        </div>
    </div>
    <div class = "userReviewsWrapper">
        <div class = "reviewName">
            {{ user.Item.UserID }}'s Reviews:
        </div> 

        <div v-if="user.Item.reviews.length != 0">
          <ReviewItem     
              v-for="review in user.Item.reviews" 
              :key = "review.id" 
              :username = "user.Item.UserID" 
              :review = "review" 
              @favorite = "toggleFavorite"
          />
        </div>
        <div v-else> Nothing yet :)</div>

    </div>
    <!--
        <div class = "followButton">
            <button v-on:click="followUser">
                Follow
            </button>
        </div>
    -->
        <div class = "logoutButton">
            <button v-on:click="logout">
                Logout
            </button>
        </div>
    </div>
  </div>
</template>

<script>
import { reactive, watch, computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute, useRouter } from 'vue-router';
import ReviewItem from "../components/ReviewItem.vue"
import Profile from "../views/Profile";

export default {
  name: 'UserProfile',
  components: { ReviewItem, Profile },  
  setup() {
      const store = useStore();
      const route = useRoute();
      const router = useRouter();
      const userId = computed(() => route.params.userId)
      const user = computed(() => store.state.User.user);

    // 5.6: Add stats to user like average rating, past likes, total likes, etc. I think we should remove followers and just have average review rating and number of ratings. That way famous people's opinions wouldnt be more important
    // 9: Add security to passwords
    // ?: add a show less after expanding review
    // ?: Be able to edit specific values of your review - could be added as a separate page, linked to by both profile and post
    // ?: Add click outside functionality for dropdown boxes
    // ?: Order the reviews in reverse-id order so the newest is at front

    // else: Deploy app as website, get user testing
    // eventually: 
    // fix the "nothing yet :)" from showing bc it takes a sec to load
    // Gradually load reviews on browse instead of all at once
    // Add redirects to homepage/browse when necessary (right domain, wrong extension | or review that doesnt exist, etc)
    // Make it look really nice
    // doesnt check to see if every field is full on registration

    // BY PRESENTATION DAY
    // delete/edit review
    //    ^--> this requires a drop-down box when clicking review. Asks for edit or delete. Edit will have to be it's own component. Data sent to flask will replace every value in current review, then entered. Delete asks if you are sure  
 

      const state = reactive({
        followers: 0,
        userTestVal: '',
        notLoggedIn: false,
        UserID: userId.value
      })

      // calls Profile component when not logged in. So the state is not set to an unlogged in user
      if(user.value === null) {
        state.notLoggedIn = true,
        state.userTestVal = user.value
      }
      else {
        state.userTestVal = user.value.Item.UserID
        state.UserID = userId.value
      }

      function toggleFavorite(id) {
        console.log(`Favorited Review = ${id}`)
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
        toggleFavorite,
        userId,
        logout,
        user
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
