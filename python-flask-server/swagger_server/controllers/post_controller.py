import connexion
import six
import sqlite3

from swagger_server.models.full_post import FullPost  # noqa: E501
from swagger_server.models.post import Post  # noqa: E501
from swagger_server import util
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def create_post(body):  # noqa: E501
    """Add a new post to the blog

     # noqa: E501

    :param body: Post object that needs to be added to the blog
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Post.from_dict(connexion.request.get_json())  # noqa: E501
        title = body.title
        content = body.content
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
    return


def delete_post(postId):  # noqa: E501
    """Delete post

    Delete post # noqa: E501

    :param postId: ID of post to delete
    :type postId: int

    :rtype: Post
    """
    post = get_post(postId)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (postId,))
    conn.commit()
    conn.close()
    return post


def edit_post(postId, body):  # noqa: E501
    """Edit post

    Edit post # noqa: E501

    :param postId: ID of post to edit
    :type postId: int
    :param body: Post object that needs to be added to the blog
    :type body: dict | bytes

    :rtype: Post
    """
    if connexion.request.is_json:
        body = Post.from_dict(connexion.request.get_json())  # noqa: E501
        post = get_post(postId)
        title = body.title
        content = body.content
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?'
                        ' WHERE id = ?',
                     (title, content, postId))
        conn.commit()
        conn.close()
        return post


def get_post_by_id(postId):  # noqa: E501
    """Get post by ID

    Returns a single post # noqa: E501

    :param postId: ID of post to return
    :type postId: int

    :rtype: Post
    """
    return get_post(postId)


def get_posts():  # noqa: E501
    """Get all posts

    Returns all posts # noqa: E501


    :rtype: FullPost
    """
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts
