<template>
<div v-if="edit == true" class = "userProfileReview">
  <div class = "userReviewItem">
    <div class = "reviewContext"> 
      <div class = "reviewItemContent">
  <div>
    <form @submit.prevent="handleSubmit(review.id)">
            <span>Artist - &nbsp;</span>
            <input type="text" class="text" v-model="state.review.artist" name="artist">
            <br>
            <span>Album - &nbsp;</span>
            <input type="text" class="text" v-model="state.review.album" name="album">
            <br>
            <span>Songname - &nbsp;</span>
            <input type="text" class="text" v-model="state.review.songname" name="songname">
            <br>
            <span>Content -</span>
            <input type="text" class="text" v-model="state.review.content" name="content">
            <br>
            
            <!-- if edited, show button, else just have back button -->
            <br>
            <button class="button">Submit Changes</button>

  <!--       <div v-show="state.invalid">
            <div class="invalid">Invalid edit to submit</div>
          </div>
    -->
    </form>
  </div>
</div>
</div>
</div>
</div>

<!-- for delete -->
<div v-else>
does this show up
</div>
</template>

<script>
import { reactive, onMounted } from "vue";
import { useStore } from 'vuex';

export default {
    name: "Edit",
    setup(props, ctx) {
        // make sure accesssing outside of substring doesn't break it. Doesn't seem to right now.
        // Adds functionality for expanding reviews
        const store = useStore();
        const state = reactive({
            edit: false,
            username:  '',
            review:  [],
            invalid: false
        });

        function showOptions(id) {
            ctx.emit("showOptions", id);
        }

        onMounted(() => {
          state.username = props.username;
          props.edit == false;
          state.review = props.review
        })

      function handleSubmit() {
      // scuffed because I can't call await methods without it being in a const function
      // converts review id into int, is string. Need to figure out why this happens but for now I want it fixed.
        state.review.id = parseInt(state.review.id)
        const data = [props.review, state.username]
        console.log("data")
        console.log(data)
        commitReview(data);
      }

      const commitReview = async (data) => {
        await fetch('http://3.133.58.37:5000/edit', {
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
        return {
            handleSubmit,
            showOptions,
            commitReview,
            setUser,
            state
        };
    },
    props: {
        username: {
            type: String,
            required: true
        },
        review: {
            type: Object,
            required: true
        },
        edit: {
            type: Boolean,
            required: true
        }
    },
};
</script>

<style lang="scss" scoped>
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
    //font-size: 18px;   --> if I use serif instead of arial

    .userReviewItem {
        font-weight: bold;
    }

    .reviewContext {
        font-weight: normal;
    }

    input[type=text] {
      background-color: #ececec;
      font-family: Avenir, Helvetica, Arial, sans-serif;
      color: #0d1424;
      border: none;
      font-size: 16px;  
    }

    textarea {
      background-color: #ececec;
      font-family: Avenir, Helvetica, Arial, sans-serif;
      color: #0d1424;
      border: none;
      font-size: 18px;  
      resize: none;
      text-align: center;
    }

    input[type=text]:focus {
      background-color: #ececec;
      font-family: Avenir, Helvetica, Arial, sans-serif;
      color: #0d1424;
      border: none;
      font-size: 18px;    
    }

    text {
      font-size: 16px;  
      text-align: center; 
    }
}
</style>