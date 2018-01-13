import express from 'express'
import webpack from 'webpack'
import config from './webpack.config.dev.js'

const port = process.env.WEBPACK_PORT || 9000
const compiler = webpack(config)

const serverOptions = {
  contentBase: `http://localhost:${port}`,
  compress: true,
  quiet: true,
  noInfo: true,
  hot: true,
  inline: true,
  lazy: false,
  publicPath: config.output.publicPath,
  headers: { 'Access-Control-Allow-Origin': '*' },
  stats: { colors: true },
  historyApiFallback: true
}

const app = express()

app.use(require('webpack-dev-middleware')(compiler, serverOptions))
app.use(require('webpack-hot-middleware')(compiler))

app.listen(port, (err) => {
  if (err) {
    console.error(err)
  } else {
    console.info('==> 🚧  Webpack development server listening on port %s', port)
  }
})
