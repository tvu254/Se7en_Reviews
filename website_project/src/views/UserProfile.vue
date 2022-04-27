<template>
  <Profile v-if="state.notLoggedIn || ((state.UserID != state.userStateVal))"/>
  <div v-else>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <div class = "userProfilePanel">
            <h1 class = "userProfileUsername">{{ userId }}</h1>
            <h1> &nbsp; AKA </h1>
            <h1> {{ user.Item.firstName }} {{ user.Item.lastName }} </h1>
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
        <br>
          <div class = "logoutButton">
            <button class = "button" v-on:click="logout">
                Logout
            </button>
        </div>
    </div>
    <div class = "userReviewsWrapper">
        <div class = "reviewName">
            Your Reviews
        </div>

        <div v-if="user.Item.reviews.length != 0">
          <ReviewItem
              v-for="review in user.Item.reviews"
              :key = "review.id"
              :username = "user.Item.UserID"
              :loggedIn = "true"
              :review = "review"
              @deleteReview = "deleteReview"
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


    // 9: Add security to passwords
    // ?: require first two sections on post to prevent garbage
    // ?: youtube links? if song, link + lyrics, maybe at genius? USE MY BOT CODE WITH YOUTUBE-DL - show auto-fo>
    // ?: album art / artist / relevant --> store image url, if not loaded = blank
    // ?: search


    // eventually:
    // Gradually load reviews on browse instead of all at once --> look up load on scroll --> https://www.youtub>
    // Add redirects to homepage/browse when necessary (right domain, wrong extension | or review that doesnt ex>
    // ?: Add click outside functionality for dropdown boxes
    // if not logged in block any /profile domains
    // profile.vue uses login fetch
    // /user/userID is useless rn btw

    // BY PRESENTATION DAY
    // ssl certs
    // 5.6: Add stats to user like average rating, past likes, total likes, etc. I think we should remove follow>
    // ?: Order the reviews in reverse-id order so the newest is at front
    // keep me signed in
    // refresh still logs you out
    // Make it look really nice
    // if read more not necessary, dont put. if (110 long) for example
    // dont allow sign-in to be clicked if empty
    // edit does not show the whole content box

      const state = reactive({
        followers: 0,
        userStateVal: '',
        notLoggedIn: false,
        UserID: userId.value
      })

      // calls Profile component when not logged in. So the state is not set to an unlogged in user
      if(user.value === null) {
        state.notLoggedIn = true,
        state.userStateVal = user.value
      }
      else {
        state.userStateVal = user.value.Item.UserID
        state.UserID = userId.value
      }

      function deleteReview(id) {
      // scuffed because I can't call await methods without it being in a const function
        const data = [id, user.value.Item.UserID]
        console.log("data")
        console.log(data)
        sendDelete(data);
      }

      const sendDelete = async (data) => {
        await fetch('http://3.133.58.37:5000/delete', {
        method: 'POST',
        body: JSON.stringify({ data }),
        headers: {
            'Content-type': 'application/json',
        }
        })
        .then((response) => response.json())        // flask returns a response object
        .then(function (user) {
            console.log(user);        // error catch is based on response. Not sure if works --> Also also needs>
            setUser(user)
        })
        .catch(function (error) {
          console.warn('Something went horribly wrong -->', error);
        });
      }

      // for updating state-user according to database
      const setUser = async (user) => {
        await store.dispatch('User/setUser', user);
        console.log(user.Item.username)
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
        deleteReview,
        setUser,
        userId,
        logout,
        sendDelete,
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