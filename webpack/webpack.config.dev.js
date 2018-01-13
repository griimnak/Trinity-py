import webpack from 'webpack'
import path from 'path'

const port = process.env.WEBPACK_PORT || 9000
const publicPath = `http://localhost:${port}/dist/`
const appName = 'Trinity3'

const srcPath = path.resolve(__dirname, '..', 'src')
const trinityPath = path.join(srcPath, 'index.js')
const outputFile = appName.toLowerCase() + '.js'

export default {
  devtool: 'inline-source-map',
  entry: [
    `webpack-hot-middleware/client?path=http://localhost:${port}/__webpack_hmr`,
    trinityPath,
  ],
  output: {
    path: path.resolve(__dirname, '..', 'pub', 'js'),
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
        include: srcPath,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    modules: [
      srcPath,
      'node_modules'
    ],
    extensions: ['.json', '.js']
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NamedModulesPlugin(),
  ]
}