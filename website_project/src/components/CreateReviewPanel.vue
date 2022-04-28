<template>
  <form class = "createReviewPanel" @submit.prevent = "createNewReview" :class="{ '--exceeded': newReviewCharacterCt > 2000 }">  <!-- stop submit button when > 2000 -->


    <div class="createReviewPanelSubmit">
      <div class = "createReviewType">

        <!--        <label for="newReviewType"> <strong>Type: </strong> </label>
                    <select id = "newReviewType" v-model = "state.selectedReviewType">
                        <option :value = "option.value" v-for = "(option, index) in state.reviewTypes" :key = "index">
                            {{ option.name }}
                        </option>
                    </select>
                    <br>
        -->
        <label for="newGenre"> <strong>Genre</strong> </label>
        <br>
        <select id = "newGenre" v-model = "state.selectedGenre">
          <option :value = "option.value" v-for = "(option, index) in state.genres" :key = "index">
            {{ option.name }}
          </option>
        </select>
        <br>
        <label for = "newReview"> <strong>Artist</strong></label>
        <textarea id="newReview" rows = "1" v-model = "state.newArtistContent"/>
        <br>
        <label for = "newReview"> <strong>Album</strong></label>
        <textarea id="newReview" rows = "1" v-model = "state.newAlbumContent"/>
        <br>
        <label for = "newReview"> <strong>Song Name</strong>  </label>
        <textarea id="newReview" rows = "1" v-model = "state.newSongNameContent"/>
        <br>
        <label for = "newReview"> <strong>New Review &emsp;</strong>
          {{ newReviewCharacterCt }} &nbsp; / &nbsp; 2000
        </label>
        <textarea id="newReview" rows = "8" v-model = "state.newReviewContent"/>
        <br>
        <hr>
        <button class = "button"> <strong>Post Review</strong></button>
        <br>
        <div v-if="newReviewCharacterCt > 2000">Limit Exceeded!</div>
      </div>
    </div>
  </form>
</template>

<script>
import { reactive, computed } from 'vue';

export default {
  name: "CreateReviewPanel",
  setup(props, ctx) {
    const state = reactive({
      exceeded: false,
      newReviewContent: '',
      newArtistContent: '',
      newAlbumContent: '',
      newSongNameContent: '',
//            selectedReviewType: 'choose',
      selectedGenre: 'choose',
//            reviewTypes: [
//                { value: 'choose', name: 'Choose' },
//                { value: 'music', name: 'Music' },
      //{ value: 'game', name: 'Game' },
      //{ value: 'movie', name: 'Movie' }
//            ],

      // will eventually need to display differently depending on what review type is chosen
      genres: [
        { value: 'choose',              name: 'Choose' },
        { value: 'indie/Alternative',   name: 'Indie/Alternative' },
        { value: 'rock',                name: 'Rock' },
        { value: 'hip-Hop',             name: 'Hip-Hop' },
        { value: 'metal',               name: 'Metal' },
        { value: 'soul',                name: 'Soul' },
        { value: 'pop',                 name: 'Pop' },
        { value: 'classical',           name: 'Classical' },
        { value: 'alternative-Rock',    name: 'Alternative-Rock' },
        { value: 'latin',               name: 'Latin' },
        { value: 'funk',                name: 'Funk' },
        { value: 'bluegrass',           name: 'Bluegrass' },
        { value: 'experimental',        name: 'Experimental' },
        { value: 'grunge',              name: 'Grunge' },
        { value: 'jazz',                name: 'Jazz' },
        { value: 'blues',               name: 'Blues' },
        { value: 'country',             name: 'Country' },
        { value: 'dubstep',             name: 'Dubstep' }
      ]
    })

    const newReviewCharacterCt = computed(() => state.newReviewContent.length)

    function createNewReview() {
      // converts review data into list to be sent (emitted) to addReview function in userProfile
      if (newReviewCharacterCt.value <= 2000) {
        var newReviewList = [state.newReviewContent, state.selectedGenre, state.newArtistContent, state.newAlbumContent, state.newSongNameContent, new Date()]

        if (state.newReviewContent !== 'choose') {
          ctx.emit('add-review', newReviewList);
          state.newReviewContent = '';
          state.newArtistContent = '';
          state.newAlbumContent = '';
          state.newSongNameContent = '';
        }
        state.newReviewContent = '';
      }
      else {
        state.exceeded = true
      }
    }

    return {
      state,
      newReviewCharacterCt,
      createNewReview
    }
  }
};
</script>

<style lang = "scss" scoped>

//* {box-sizing: border-box}

.createReviewPanel {
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  //border: 1px solid;
  //border-color: red;


  textarea {
    border: 1px solid black;
    //#DFE3E8;
    border-radius: 5px;
    background: white;
    width: 100%;
    resize: vertical;
    overflow: auto;
  }

  hr {
    margin-bottom: 10px;
  }

  .createReviewPanelSubmit {
    display: flex;
    justify-content: space-between;
    background-color: #ececec;
    border: 1px solid black;
    padding: 30px;
    border-radius: 5px;
    width: 100%;


    .createReviewType {
      border-radius: 5px;
      flex-direction: column;
      box-sizing: border-box;
      text-align: center;
      margin-top: 10px;
    }
    .button {
      //max-height: 50px;
      padding: 16px 20px;
      margin: 8px 0;
      border: 1px solid black;
      cursor: pointer;
      width: 100%;
      opacity: 0.9;
      font-size: 18px;
    }
  }

  &.--exceeded {
    color: red;
    border-color: rgb(145, 67, 182);

    .createReviewPanelSubmit {
      button {
        background-color: red;
        color: #b9b9b9;
      }
    }
  }
}

</style>
