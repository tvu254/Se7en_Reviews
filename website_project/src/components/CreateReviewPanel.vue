<template>
<form class = "createReviewPanel" @submit.prevent = "createNewReview" :class="{ '--exceeded': newReviewCharacterCt > 2000 }">  <!-- stop sumbit button when > 2000 -->
    <label for = "newReview"> <strong>New Review</strong> - ({{ newReviewCharacterCt }}/2000)  </label>
    <textarea id="newReview" rows = "4" v-model = "state.newReviewContent"/>

  <div class="createReviewPanelSubmit">
    <div class = "createReviewType">
        <label for="newReviewType"> <strong>Type: </strong> </label>
        <select id = "newReviewType" v-model = "state.selectedReviewType">
            <option :value = "option.value" v-for = "(option, index) in state.reviewTypes" :key = "index">
                {{ option.name }}
            </option>
        </select>
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
            selectedReviewType: 'choose',
            reviewTypes: [
                { value: 'choose', name: 'Choose' },
                { value: 'music', name: 'Music' },
                { value: 'game', name: 'Game' },
                { value: 'movie', name: 'Movie' }
            ]
        })

        const newReviewCharacterCt = computed(() => state.newReviewContent.length)

        function createNewReview() {
            // converts review data into list to be sent (emitted) to addReview function in userProfile
            var newReviewList = [state.newReviewContent, state.selectedReviewType]

            if (state.newReviewContent && state.selectedReviewType !== 'choose') {
                ctx.emit('add-review', newReviewList);
                state.newReviewContent = '';
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