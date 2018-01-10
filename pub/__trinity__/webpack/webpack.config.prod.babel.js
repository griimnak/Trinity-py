import webpack from 'webpack'
import path from 'path'

const port = process.env.WEBPACK_PORT || 9000
const publicPath = `http://localhost:${port}/dist/`
//const env = process.env.WEBPACK_ENV
const appName = 'Trinity3'
const plugins = []

const trinityPath = path.join(__dirname, '..', 'src')
const outputFile = appName.toLowerCase() + '.min.js'

export default {
  devtool: 'inline-source-map',
  entry: [
    'babel-polyfill',
    trinityPath,
  ],
  output: {
    path: path.resolve(__dirname, '..', 'build'),
    filename: outputFile,
    library: appName,
    libraryTarget: 'umd',
    umdNamedDefine: true,
    publicPath
  },
  module: {
    rules: [
      {
        test: /(\.jsx|\.js)$/,
        include: path.join(__dirname, '..', 'src'),
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    modules: [
      path.resolve(__dirname, '..', 'src'),
      'node_modules'
    ],
    extensions: ['.json', '.js']
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NamedModulesPlugin(),
    new webpack.optimize.UglifyJsPlugin({ minimize: true })
  ]
}
