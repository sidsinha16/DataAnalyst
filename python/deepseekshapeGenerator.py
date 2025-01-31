from gradio_client import Client, handle_file

client = Client("tencent/Hunyuan3D-2")
result = client.predict(
		caption="Hello!!",
		image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		steps=50,
		guidance_scale=5.5,
		seed=1234,
		octree_resolution="256",
		check_box_rembg=True,
		api_name="/shape_generation"
)
print(result)