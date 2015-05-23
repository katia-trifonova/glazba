
var less = require('gulp-less'),
    path = require('path');

gulp.task('less', function () {
  gulp.src('../less/style.less')
    .pipe(less())
    .pipe(gulp.dest('../css/st.css'));
});
