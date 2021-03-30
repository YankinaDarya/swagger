# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.full_post import FullPost  # noqa: E501
from swagger_server.models.post import Post  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostController(BaseTestCase):
    """PostController integration test stubs"""

    def test_create_post(self):
        """Test case for create_post

        Add a new post to the blog
        """
        body = Post({title: "test title", content: "test content"})
        response = self.client.open(
            '/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_post(self):
        """Test case for delete_post

        Delete post
        """
        response = self.client.open(
            '/myPosts/{postId}/delete'.format(postId=2),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_post(self):
        """Test case for edit_post

        Edit post
        """
        body = Post({title: "new title", content: "new content"})
        response = self.client.open(
            '/myPosts/{postId}/edit'.format(postId=2),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_post_by_id(self):
        """Test case for get_post_by_id

        Get post by ID
        """
        response = self.client.open(
            '/myPosts/{postId}'.format(postId=3),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_posts(self):
        """Test case for get_posts

        Get all posts
        """
        response = self.client.open(
            '/myPosts',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
