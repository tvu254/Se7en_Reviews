<template>
    <div class = "userProfile">
      <div class="userProfileSidebar">
        <CreateReviewPanel @add-review="addReview"/>
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
              :loggedIn = "true"
              :review = "review" 
              @deleteReview = "deleteReview"
          />
        </div>
        <div v-else> Nothing yet :)</div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import ReviewItem from "../components/ReviewItem.vue"
import CreateReviewPanel from "../components/CreateReviewPanel.vue";

export default {
  name: 'UserProfile',
  components: { CreateReviewPanel, ReviewItem },
  setup() {

      const store = useStore();
      const route = useRoute();
      const user = computed(() => store.state.User.user);
      const userId = computed(() => route.params.userId)

      function deleteReview(id) {
      // scuffed because I can't call await methods without it being in a const function
        const data = [id, user.value.Item.UserID]
        sendDelete(data);
      }

      const sendDelete = async (data) => {
        await fetch('http://localhost:5000/delete', {
        method: 'POST',
        body: JSON.stringify({ data }),     
        headers: {
            'Content-type': 'application/json',
        }
        })
        .then((response) => response.json())        // flask returns a response object
        .then(function (user) {
            console.log(user);        // error catch is based on response. Not sure if works --> Also also needs to update the state-user
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

      function getNewID(newID) {
        // gets next highest id number for new review. Does not double as total review # bc user can delete highest-ID review
        let highestID = 0;
        for(let i = 0; i < user.value.Item.reviews.length; i++) {
          if(user.value.Item.reviews[i].id > highestID) {
            newID = user.value.Item.reviews[i].id;
            highestID = newID
          }
        }
        newID = parseInt(newID) + 1
        return newID;
      }

      function addReview(newReviewList) {
        newReviewList[1] = newReviewList[1].charAt(0).toUpperCase() + newReviewList[1].slice(1);
        newReviewList[2] = newReviewList[2].charAt(0).toUpperCase() + newReviewList[2].slice(1);
        newReviewList[3] = newReviewList[3].charAt(0).toUpperCase() + newReviewList[3].slice(1);
        newReviewList[4] = newReviewList[4].charAt(0).toUpperCase() + newReviewList[4].slice(1);

        let newID = 0;
        newID = getNewID(newID);

        user.value.Item.reviews.unshift( {
            id: newID,
            content: newReviewList[0],
            genre: newReviewList[1],
            artist: newReviewList[2],
            album: newReviewList[3],
            songname: newReviewList[4],
            dateCreated: newReviewList[5],

        });
        saveReview([user.value.Item.reviews[0], user.value.Item.UserID])
    }

      const saveReview = async (review) => {
        console.log(review)
        await fetch('http://localhost:5000/post', {
          method: 'POST',
          body: JSON.stringify({ review }),
          headers: {
            'Content-type': 'application/json',
          }
        })
        .then((response) => response.json())
        .then(function (data) {
          console.log(typeof(data))             // flask returns a response object
        })
        .catch(function (error) {
          console.warn('Something went horribly wrong.', error);
        });
      };


    return {
        addReview,
        deleteReview,
        sendDelete,
        userId,
        saveReview,
        setUser,
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