import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    observedState: "",
    isUpdate: false
  },
  mutations: {
    updateObservedState(state, observedState) {
      state.observedState = observedState
    },
    updateIsUpdate(state, isUpdate) {
      state.isUpdate = isUpdate
    }
  },
  getters: {
    getObservedState(state) {
      return state.observedState
    },
    getIsUpdate(state){
      return state.isUpdate
    }
  }
});
