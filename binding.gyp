{
	"targets": [
		{
			"target_name": "knxclient",
			"sources": [
				"lib/knxclient.cpp",
				"lib/util.cpp"
			],
			"cflags": [
				"-std=c++11"
			],
			"ldflags": [
				"-lknxclient"
			]
		}
	]
}
