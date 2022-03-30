<template>
<form class = "createReviewPanel" @submit.prevent = "createNewReview" :class="{ '--exceeded': newReviewCharacterCt > 2000 }">  <!-- stop submit button when > 2000 -->

    <label for = "newReview"> <strong>New Review:</strong></label>
    <textarea id="newReview" rows = "8" v-model = "state.newReviewContent"/>

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
        <label for="newGenre"> <strong>Genre: </strong> </label>
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

    </div>
    <button >
        Post Review
    </button>
  </div>
</form>
</template>

<script>
import { reactive, computed } from 'vue';

export default {
    name: "CreateReviewPanel",
    setup(props, ctx) {
        const state = reactive({
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
            var newReviewList = [state.newReviewContent, state.selectedGenre, state.newArtistContent, state.newAlbumContent, state.newSongNameContent, new Date()]

            if (state.newReviewContent !== 'choose') {
                ctx.emit('add-review', newReviewList);
                state.newReviewContent = '';             // eventually needs to not reset when characters > character limit, if it goes thru, reset fields
                state.newArtistContent = '';
                state.newAlbumContent = '';
                state.newSongNameContent = '';
            }
            state.newReviewContent = '';
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
.createReviewPanel {
    padding-top: 20px;
    display: flex;
    flex-direction: column;
    

    textarea {
        border: 1px solid #DFE3E8;
        border-radius: 5px;
    }

    .createReviewPanelSubmit {
        display: flex;
        justify-content: space-between;
        

        .createReviewType {
            border-radius: 5px;
            flex-direction: column;
            box-sizing: border-box;
            text-align: center;
            margin-top: 10px;
        }

        button {
            padding: 5px 20px;
            margin: auto 0;
            margin-top: 7px;
            border: 1px #cc26a2;
            border-radius: 5px;
            background-color: #b9b9b9;
            color: #0d1424;
            font-weight: bold;
            cursor: pointer;
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