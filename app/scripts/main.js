var detector = new FaceDetector('detection');

var app = new Vue({
  el: '#app',
  data () {
    return {
        detector: detector

    }
  },
  /* Method Definition  */
  methods: {
      
      // Load App method
      loadApp: function(app) {
          this.detector.loadApp(app);
      },
      
      continuousMethod: function(facedetector) {
          console.log(facedetector.app.detections);
      },
      
      callbackMethod: function(facedetector) {
         
        //<---- do whatever you want here
          console.log('Example of what can be done');
        
       
         
      }
      
  },
 
  mounted () {
      
      
      
  }

});
