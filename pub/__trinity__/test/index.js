import Trinity3 from './trinity3'

Trinity3()

if (module.hot) {
  module.hot.accept('./trinity3', () => {
    require('./trinity3')()
  })
}
