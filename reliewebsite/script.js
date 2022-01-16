import './style.css'

import * as THREE from 'three';

import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';


const scene = new THREE.Scene();


const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector('#bg'),
});

renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );
camera.position.setZ(50);
camera.position.setX(20);

renderer.render( scene, camera );

const geometry = new THREE.TorusGeometry( 10, 3, 16, 100)
const material = new THREE.MeshBasicMaterial( { color: 0xdb451f, wireframe: true } );
const torus = new THREE.Mesh( geometry, material );

scene.add(torus)

const controls = new OrbitControls(camera, renderer.domElement);

function moveCamera() {

const t = document.body.getBoundingClientRect().top;
camera.position.z = t * 0.02;
camera.position.z = t * -0.02
}

document.body.onscroll = moveCamera

function animate() {
  requestAnimationFrame( animate );

  torus.rotation.z += 0.003;
  
  
 

  controls.update();

  renderer.render( scene, camera );
}

animate()