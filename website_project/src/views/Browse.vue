<template>
  <div class="browse">
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
                />
                <br>
                <br>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
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
            fetch('http://localhost:5000/browse', {
                method: "GET",
            })
            .then(resp => resp.json())
            .then(data => {
                // will eventually need to gradually load reviews so it doesnt overwhelm, this loads the whole table --> see vid about scrolling to load
                for(let i = 0; i < (data.Items.length); i++) {
                    userList.unshift(data.Items[i])
                }
                state.loaded = true
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
.browse {
    padding: 50px 5%;
    text-align: center;
}

.reviewItem {
    padding: 12px;
    background-color: #ececec;
    border-radius: 5px;
    border: 1px solid #0d1424;
    box-sizing: border-box;
    cursor: pointer;
    transition: all 0.24s ease;
    width: 550px;
    margin: auto;
    margin-top: 5px;
    text-align: center;
    //font-size: 18px;   --> if I use serif instead of arial

    &:hover {
        transform: scale(1.1, 1.1);
    }

    .userReviewItem {
        font-weight: bold;
    }

    .reviewContext {
        font-weight: normal;
    }
}

</style>