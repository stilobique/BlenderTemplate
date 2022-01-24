import docker


def clear_container_test(tag: str = 'stilobique/blender:latest'):
    client = docker.from_env()
    containers = client.containers.list(all=True)

    for container in containers:
        image_tag = container.image.tags[0]
        status = container.status
        if image_tag == tag and status == 'exited':
            container.remove()


if __name__ == '__main__':
    # Clear all unused blender container
    clear_container_test()
