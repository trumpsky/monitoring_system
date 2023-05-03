import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    observedState: "",
    isUpdate: false,
    algorithm: ""
  },
  mutations: {
    updateObservedState(state, observedState) {
      state.observedState = observedState
    },
    updateIsUpdate(state, isUpdate) {
      state.isUpdate = isUpdate
    },
    updateAlgorithm(state, algorithm) {
      state.algorithm = algorithm
    }
  },
  getters: {
    getObservedState(state) {
      return state.observedState
    },
    getIsUpdate(state){
      return state.isUpdate
    },
    getAlgorithm(state){
      return state.algorithm
    }
  }
});
