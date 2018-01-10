import { Component, helpers } from 'trinity-web'

export default class LastPage extends Component {

  initialState = ({ store }) => {
    const mocky = store.get('mocky')

    return {
      mocky: !!mocky ? mocky : null
    }
  }

  async afterRender({ store, state, context: { api } }) {
    if (!state.mocky) {
      try {
        const result = await api.get('https://www.mocky.io/v2/5185415ba171ea3a00704eed')

        store.set({ mocky: { result } })
        this.setState({ mocky: { result } })
      } catch (error) {
        this.setState({ mocky: { error } })
      }
    }
  }

  render = ({ state, store }) => {
    console.log('render', store.get())

    const { lastPage: { name, url } } = store.get()

    return state.mocky
      ? `<a href="${url}" data-navigate>
            ${name}
         </a>`
      : `<div>Loading</div>`
  }

}