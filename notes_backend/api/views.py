from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """
    Health check endpoint.
    Returns 200 OK with a simple message to indicate the server is running.
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class NoteListCreateAPIView(generics.ListCreateAPIView):
    """
    list:
    Retrieve a paginated list of notes. Supports filtering by:
    - q: case-insensitive search in title or content
    - is_archived: accepts 1/true/yes or 0/false/no

    create:
    Create a new note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        """
        Optionally filter notes by query string `q` and `is_archived` flag.
        """
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        archived = self.request.query_params.get('is_archived')

        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))

        if archived is not None:
            val = archived.lower()
            if val in ['1', 'true', 'yes']:
                qs = qs.filter(is_archived=True)
            elif val in ['0', 'false', 'no']:
                qs = qs.filter(is_archived=False)

        return qs


# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve:
    Get a single note by ID.

    update:
    Update a note fully or partially.

    destroy:
    Delete a note by ID.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
