import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    observedState: ""
  },
  mutations: {
    updateObservedState(state, observedState) {
      state.observedState = observedState
    }
  },
  getters: {
    getObservedState(state) {
      return state.observedState
    }
  }
});
