var gulp = require("gulp");
var $    = require("gulp-load-plugins")();

var sassPaths = [
	"bower_components/normalize.scss/sass",
	"bower_components/foundation-sites/scss",
	"bower_components/motion-ui/src",
	"bower_components/font-awesome/scss"
];

gulp.task("sass", function(){
	return gulp.src("scss/app.scss")
		.pipe($.sass({
			includePaths: sassPaths,
			outputStyle: "compressed" // if css compressed **file size**
		})
			.on("error", $.sass.logError))
		.pipe($.autoprefixer({
			browsers: ["last 2 versions", "ie >= 9"]
		}))
		.pipe($.rename("opsoro.css"))
		.pipe(gulp.dest("css"));
});

var js_common = [
	"bower_components/foundation-sites/dist/js/foundation.js",
	"bower_components/jquery/dist/jquery.js",
	"bower_components/knockout/dist/knockout.js",
	"bower_components/what-input/dist/what-input.js"
];

gulp.task("js-common", function(){
	return gulp.src(js_common)
		.pipe($.concat("opsoro-common.js"))
		.pipe($.minify({
			ext: {
				min: ".js"
			}
		}))
		.pipe(gulp.dest("js"));
});

var js_libs = [
	"bower_components/svg.js/dist/svg.min.js",
	"bower_components/sockjs-client/dist/sockjs.min.js",
	"bower_components/numeraljs/min/numeral.min.js",
	"bower_components/numeraljs/min/locales.min.js",
	"bower_components/knockout-sortable/knockout-sortable.min.js",
	"bower_components/jcanvas/jcanvas.min.js",
	"bower_components/flot/jquery.flot.*.js",
	"bower_components/flot/jquery.flot.js"
];

gulp.task("js-libs", function(){
	return gulp.src(js_libs)
		.pipe(gulp.dest("js/vendor/"));
});

gulp.task("assets", function(){
	var t1 = gulp.src("bower_components/font-awesome/fonts/*")
		.pipe(gulp.dest("fonts"));
	//var t2 = gulp.src();

	//return [t1, t2];
	return t1
});

// gulp.task("watch", ["sass"], function(){
// 	gulp.watch(["scss/**/*.scss"], ["sass"]);
// });

gulp.task("default", ["sass", "js-common", "js-libs", "assets"]);