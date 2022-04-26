<template>
  <div class="homeAnnouncement">
    <h1><strong>Welcome to uReview!</strong></h1>
    <h2> This is the uReview alpha version. Feel free to explore login, browse, and post features :) - Comments, ratings, search, review editing, as well as stylistic updates are coming soon. Thank you for visiting!
    </h2>
    <br>

    <div class="homeReleases">
     <h1>Upcoming Releases</h1>
  <img src="../assets/zeit.jpg" alt="Zeit by Ramnstein" style="width:12.5%">
  <img src="../assets/voltage.jpg" alt="Voltage by Itzy" style="width:12.5%">
  <img src="../assets/kdm.jpg" alt="Voltage by Itzy" style="width:12.5%">
  <img src="../assets/ineverdie.jpg" alt="Voltage by Itzy" style="width:12.5%">
  <img src="../assets/htcs.jpg" alt="Voltage by Itzy" style="width:12.5%">
</div>

    <div class="userList">
    <strong>Featured Reviews</strong>
    <br>
    <br>
  </div>

<!--  For reference later
      <div v-show="state.loaded">
        <router-link v-for="user in userList" :to="{ name: 'UserProfile', params: {userId: user.UserID} }" :key="user.UserID">
          {{ user.username }}
        </router-link>
      </div>
-->

      <div v-show="state.loaded">
        <div v-for="user in userList" :key = "user.reviews">
          <div v-if="user.reviews.length != 0">
            <router-link :to="`/user/${user.UserID}`">
              <strong>{{ user.UserID }}'s </strong>
            </router-link> 
                reviews:
                <ReviewItem     
                    v-for="review in user.reviews" 
                    :key = "review.id" 
                    :username = "UserID" 
                    :loggedIn = "false"
                    :review = "review"
                    @favorite = "toggleFavorite"
                />
                <br>
                <br>
            </div>
        </div>
    </div>
   </div>

</template>

<script>
/*
      <div v-show="state.loaded">
        <router-link v-for="user in userList" :to="{ name: 'UserProfile', params: {userId: user.userID} }" :key="user.UserID">
          {{ user.username }}
        </router-link>
      </div>
      */
import { onMounted, reactive } from "vue";
import ReviewItem from "../components/ReviewItem.vue"


export default {
    name: "Browse",
    components: { ReviewItem },
    setup() {
        onMounted(() => {
            getUsers();
        })
        let userList = []
        const state = reactive({
                loaded: false
        })

        function getUsers() {
            fetch('http://3.139.65.193/browse', {
                method: "GET",
            })
            .then(resp => resp.json())
            .then(data => {
                for(let i = 0; i < 5; i++) {
                    userList.unshift(data.Items[i])
                }
                state.loaded = true
                console.log(userList[1].reviews[1])
            })
            .catch(function (error) {
                console.warn('Something went horribly wrong.', error);
            });
        }

        return {
            getUsers,
            state,
            userList
        }
      },
    };
</script>

<style lang="scss" scoped>

.homeAnnouncement {
  position: relative;
  height: 300px;
  width: 900px;
  margin: auto;
  padding: 50px 50px;
  //background: white;
  background-size: cover;
  text-align: center;

  .userList {
    display: flex;
    flex-direction: column;
    font-size: 22px;
  }

  .homeNewReleases {
  position: relative;
  height: 100px;
  width: 250px;
  margin: auto;
  padding: 50px 50px;
  //background: white;
  background-size: cover;
  text-align: center;
}


}
</style>
