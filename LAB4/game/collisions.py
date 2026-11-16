def handle_paddle_collision(puck, paddle):
    """
    If the puck overlaps the paddle, bounce it off.
    Returns True if a collision was handled this frame.
    """
    dx = puck.x - paddle.x
    dy = puck.y - paddle.y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance < puck.radius + paddle.radius:
        # Handle the edge case where puck and paddle are at exactly
        # the same position.
        if distance == 0:
            speed = (puck.vx ** 2 + puck.vy ** 2) ** 0.5

            if speed > 0:
                nx = puck.vx / speed
                ny = puck.vy / speed
            else:
                nx = 1.0
                ny = 0.0
        else:
            # Normal vector from paddle to puck.
            nx = dx / distance
            ny = dy / distance

        # Reflect the puck's velocity across the collision normal.
        velocity_dot_normal = puck.vx * nx + puck.vy * ny
        puck.vx -= 2 * velocity_dot_normal * nx
        puck.vy -= 2 * velocity_dot_normal * ny

        # Move the puck just outside the paddle to prevent it
        # from remaining overlapped after the collision.
        separation = puck.radius + paddle.radius + 0.1
        puck.x = paddle.x + nx * separation
        puck.y = paddle.y + ny * separation

        return True

    return False
